import smartpy as sp

# wXTZ Token  Template - token used to represent investment in the Securities Contract 
# transfer function - params have been modified for testing purpose only. 
# balance and lockup values are two different values
# balance - locked = available balance

class FA12_core(sp.Contract):
    def __init__(self, **extra_storage):
        self.init(balances = sp.big_map(tvalue = sp.TRecord(approvals = sp.TMap(sp.TAddress, sp.TNat), balance = sp.TNat, locked = sp.TNat)), totalSupply = 0, **extra_storage)

    @sp.entry_point
    def transfer(self, params):
        sp.set_type(params, sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout(("from_", ("to_", "value"))))
        sp.verify(self.is_administrator(sp.sender) |
            (~self.is_paused() &
                ((params.from_ == sp.sender) |
                 (self.data.balances[params.from_].approvals[sp.sender] >= params.value))))
        self.addAddressIfNecessary(params.to_)

        sp.verify(self.data.balances[params.from_].balance >= params.value)
        
        AvailableBalance = sp.local('AvailableBalance',abs( self.data.balances[params.from_].balance - self.data.balances[params.from_].locked ))
        sp.verify(AvailableBalance.value >= params.value , message = "Available Balance is less than transfer amount")

        self.data.balances[params.from_].balance = sp.as_nat(self.data.balances[params.from_].balance - params.value)
        self.data.balances[params.to_].balance += params.value
        sp.if (params.from_ != sp.sender) & (~self.is_administrator(sp.sender)):
            self.data.balances[params.from_].approvals[sp.sender] = sp.as_nat(self.data.balances[params.from_].approvals[sp.sender] - params.value)

    @sp.entry_point
    def approve(self, params):
        sp.set_type(params, sp.TRecord(spender = sp.TAddress, value = sp.TNat).layout(("spender", "value")))
        sp.verify(~self.is_paused())
        alreadyApproved = self.data.balances[sp.sender].approvals.get(params.spender, 0)
        sp.verify((alreadyApproved == 0) | (params.value == 0), "UnsafeAllowanceChange")

        AvailableBalance = sp.local('AvailableBalance',abs( self.data.balances[sp.sender].balance - self.data.balances[sp.sender].locked ))
        sp.verify(AvailableBalance.value >= params.value , message = "Available Balance is less than approval amount")

        self.data.balances[sp.sender].approvals[params.spender] = params.value

    def addAddressIfNecessary(self, address):
        sp.if ~ self.data.balances.contains(address):
            self.data.balances[address] = sp.record(balance = 0, locked = 0,approvals = {}, )

    @sp.view(sp.TNat)
    def getBalance(self, params):
        sp.result(self.data.balances[params].balance)

    @sp.view(sp.TNat)
    def getAvailableBalance(self,params):
        sp.result(abs(self.data.balances[params].balance - self.data.balances[params].locked ))

    @sp.view(sp.TNat)
    def getAllowance(self, params):
        sp.result(self.data.balances[params.owner].approvals[params.spender])

    @sp.view(sp.TNat)
    def getTotalSupply(self, params):
        sp.set_type(params, sp.TUnit)
        sp.result(self.data.totalSupply)

    # this is not part of the standard but can be supported through inheritance.
    def is_paused(self):
        return sp.bool(False)

    # this is not part of the standard but can be supported through inheritance.
    def is_administrator(self, sender):
        return sp.bool(False)

class FA12_mint_burn(FA12_core):
    @sp.entry_point
    def mint(self, params):

        sp.set_type(params, sp.TRecord(address = sp.TAddress, value = sp.TNat))
        
        sp.verify(self.data.validator.contains(sp.sender))
        
        self.addAddressIfNecessary(params.address)

        sp.if self.data.LockedBalance.contains(params.address):

            Index = sp.local('Index',sp.len(self.data.LockedBalance[params.address]))
            self.data.LockedBalance[params.address][Index.value] = sp.record(amount = params.value, time = sp.now)
        sp.else: 
            self.data.LockedBalance[params.address] = sp.map()
            self.data.LockedBalance[params.address][0] = sp.record(amount = params.value, time = sp.now)

        self.data.balances[params.address].balance += params.value
        self.data.balances[params.address].locked += params.value
        
        self.data.totalSupply += params.value

    @sp.entry_point
    def burn(self, params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, value = sp.TNat))

        sp.verify(self.data.validator.contains(sp.sender))

        AvailableBalance = sp.local('AvailableBalance',abs( self.data.balances[params.address].balance - self.data.balances[params.address].locked ))
        sp.verify(AvailableBalance.value >= params.value , message = "Available Balance is less than burning amount")

        self.data.balances[params.address].balance = sp.as_nat(self.data.balances[params.address].balance - params.value)
        self.data.totalSupply = sp.as_nat(self.data.totalSupply - params.value)


    @sp.entry_point
    def unlockFunds(self,params):

        sp.set_type(params, sp.TRecord(address = sp.TAddress))
        
        sp.verify(self.data.LockedBalance.contains(params.address), message = "Address does not have funds LockedUp")
        
        sp.for i in self.data.LockedBalance[params.address].keys():

            sp.if sp.now > self.data.LockedBalance[params.address][i].time.add_days(sp.to_int(self.data.LockDuration)):
            
                self.data.balances[params.address].locked = abs(self.data.balances[params.address].locked - self.data.LockedBalance[params.address][i].amount)
                del self.data.LockedBalance[params.address][i]

    @sp.entry_point
    def ModifyLockup(self,params):

        sp.set_type(params, sp.TRecord(duration = sp.TNat))

        sp.verify(sp.sender == self.data.administrator, message = "Sender is not Administrator")
        sp.verify(params.duration <= 60, message="Duration parameter is greated than 60 ")

        self.data.LockDuration = params.duration
    
    @sp.entry_point
    def ValidatorOperation(self,params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, Operation = sp.TNat))

        sp.verify(sp.sender == self.data.administrator)

        sp.if params.Operation == sp.nat(1):
            self.data.validator.add(params.address) 
        sp.else: 
            sp.verify(self.data.validator.contains(params.address))
            self.data.validator.remove(params.address)

class FA12_administrator(FA12_core):
    def is_administrator(self, sender):
        return sender == self.data.administrator

    @sp.entry_point
    def setAdministrator(self, params):
        sp.set_type(params, sp.TAddress)
        sp.verify(self.is_administrator(sp.sender))
        self.data.administrator = params

    @sp.view(sp.TAddress)
    def getAdministrator(self, params):
        sp.set_type(params, sp.TUnit)
        sp.result(self.data.administrator)

class FA12_pause(FA12_core):
    def is_paused(self):
        return self.data.paused

    @sp.entry_point
    def setPause(self, params):
        sp.set_type(params, sp.TBool)
        sp.verify(self.is_administrator(sp.sender))
        self.data.paused = params

class FA12(FA12_mint_burn, FA12_administrator, FA12_pause, FA12_core):
    def __init__(self, admin):
        FA12_core.__init__(self, paused = False, administrator = admin,validator = sp.set([admin]), LockedBalance = sp.big_map(),LockDuration = sp.nat(14))

class Viewer(sp.Contract):
    def __init__(self, t):
        self.init(last = sp.none)
        self.init_type(sp.TRecord(last = sp.TOption(t)))
    @sp.entry_point
    def target(self, params):
        self.data.last = sp.some(params)

if "templates" not in __name__:
    @sp.add_test(name = "FA12 StableCoin")
    def test():

        scenario = sp.test_scenario()
        scenario.h1("FA1.2 template - WXTZ Template")

        scenario.table_of_contents()

        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.test_account("Administrator")
        alice = sp.test_account("Alice")
        bob   = sp.test_account("Robert")

        # Let's display the accounts:
        scenario.h1("Accounts")
        scenario.show([admin, alice, bob])

        token = FA12(sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))
        scenario += token
        
        scenario += token.mint(address = bob.address, value = 100).run(sender = sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"), now = sp.timestamp(100)) 
        scenario += token.mint(address = bob.address, value = 400).run(sender = sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"), now = sp.timestamp(400))
        scenario += token.unlockFunds(address = bob.address).run(sender = bob)
        scenario += token.mint(address = bob.address, value = 400).run(sender = sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"), now = sp.timestamp(400))
# KT18b68aLZji9WK8AoMhRuLGdbZEbyMrBnS8