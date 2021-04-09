import smartpy as sp

# Oracle to Fetch XTZ/USD Pair 
class USDOracle(sp.Contract):

    def __init__(self, admin):
        
        self.init(USDPrice = sp.nat(0), keysset = sp.set([admin]) , owner = admin,securities = admin, validator = sp.set([admin]))
    
    @sp.entry_point
    def feedData(self,params):
        sp.verify(self.data.keysset.contains(sp.sender), message="User Doesn't have permission to Update Price")
        
        self.data.USDPrice = params.price 
    
    @sp.entry_point
    def changeSecurities(self,params):

        sp.set_type(params, sp.TRecord(address = sp.TAddress))
        
        sp.verify(sp.sender == self.data.owner, message="Only Governance Contract will Change Securities Contract")

        self.data.securities = params.address

    @sp.entry_point
    def ValidatorOperation(self,params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, Operation = sp.TNat))

        sp.verify(sp.sender == self.data.owner, message="Only Governance Contract will ADD or REMOVE vault factory Contract ")

        sp.if params.Operation == sp.nat(1):
            self.data.validator.add(params.address) 
        sp.else: 
            sp.verify(self.data.validator.contains(params.address), message = "Address is not present in factory contract list")
            self.data.validator.remove(params.address)

    @sp.entry_point
    def addDataContributor(self,params):
        
        sp.set_type(params, sp.TRecord(contributor = sp.TAddress, Operation = sp.TNat))

        sp.verify(sp.sender == self.data.owner, message="Only Admin will update Contributor")
        
        sp.if params.Operation == sp.nat(1):
            self.data.keysset.add(params.contributor) 
        sp.else: 
            sp.verify(self.data.keysset.contains(params.contributor), message = "Address is not present as contributor")
            self.data.keysset.remove(params.contributor)
        
    @sp.entry_point
    def SecuritiesPurchase(self,params):

        sp.set_type(params, sp.TRecord(duration = sp.TNat , address = sp.TAddress))

        c = sp.contract(sp.TRecord(price = sp.TNat, duration = sp.TNat, address = sp.TAddress), self.data.securities, entry_point = "OraclePurchaseSecurity").open_some( message = "Call to purchased PUT Option contract failed")

        mydata = sp.record(price = self.data.USDPrice,duration = params.duration, address = params.address)

        sp.transfer(mydata, sp.mutez(0), c)

    @sp.entry_point
    def SecuritiesExercise(self,params):

        sp.set_type(params, sp.TRecord(owner = sp.TAddress))
        
        c = sp.contract(sp.TRecord(price = sp.TNat, owner = sp.TAddress), self.data.securities, entry_point = "OracleExerciseSecurity").open_some( message = " call to exercised security on PUT contract failed")

        mydata = sp.record(price = self.data.USDPrice,owner = params.owner)

        sp.transfer(mydata, sp.mutez(0), c)


# AMM-based CALL Options

class Securities(sp.Contract):

    def __init__(self,admin):

            self.init(
            CallOption = sp.big_map(),
            totalSupply = sp.nat(0),
            LockedSupply = sp.nat(0),
            adminAccount = sp.nat(0),
            tokenMinted = sp.nat(0),
            WithdrawFund = sp.nat(0),
            InterestRate={1:1,7:3,14:5,21:7},
            administrator = admin,
            paused = False
            )


    @sp.entry_point
    def default(self):
        
        sp.verify(sp.amount >= sp.mutez(0))
        self.data.totalSupply += sp.fst(sp.ediv(sp.amount , sp.mutez(1)).open_some( message = "unable to convert transfer amount to nat value"))

    @sp.entry_point
    def delegate(self, baker):
    
        sp.verify(sp.sender == self.data.administrator, message = "Sender is not authorized to change vault's baker")
        sp.set_delegate(baker)

    @sp.entry_point
    def PurchaseCallOption(self,params):

        sp.set_type(params, sp.TRecord(price = sp.TNat, duration = sp.TNat, order = sp.TNat, amount = sp.TNat ))

        sp.verify(sp.amount == sp.mutez(params.amount))
        sp.verify(~self.data.CallOption.contains(sp.sender), message = "CALL Options are already registered in owner's name ")
        sp.verify(~self.data.paused, message = "Contract isn't accepting new Orders")

        duration = sp.set([1,7,14,21])

        sp.verify(duration.contains(params.duration), message = "Invalid Duration for CALL Options contract")
        
        Deadline = sp.now.add_days(sp.to_int(params.duration))
        self.data.CallOption[sp.sender] = sp.record(strikePrice = params.price, options = params.order, expiry = Deadline,reward = sp.nat(0),premium = params.amount)

        # Call Oracle to Fetch Price (Adress and Duration)
        call = sp.contract(sp.TRecord(duration = sp.TNat , address = sp.TAddress), sp.address("KT1TeegbL5HrPqHivCq7Cg4Ph4y1TciFEHTm"), entry_point = "SecuritiesPurchase").open_some(message = "Oracle Call failed")
        calldata = sp.record(duration = params.duration , address = sp.sender)
        sp.transfer(calldata, sp.mutez(0), call)


    @sp.entry_point
    def OraclePurchaseSecurity(self,params):
        
        sp.set_type(params, sp.TRecord(price = sp.TNat, duration = sp.TNat, address = sp.TAddress ))

        sp.verify(sp.sender == sp.address("KT1TeegbL5HrPqHivCq7Cg4Ph4y1TciFEHTm"), message = "Sender isn't Oracle Contract")
        
        sp.verify(self.data.totalSupply > self.data.LockedSupply, message = "All Funds are locked up in existing CALL Options")

        TotalAvailable = sp.local('TotalAvailable', abs(self.data.totalSupply - self.data.LockedSupply))
        TotalAmount = sp.local('TotalAmount',self.data.CallOption[params.address].options*abs(1000000))
        
        PremiumTotal = sp.local('PremiumTotal',self.data.CallOption[params.address].options*10000*self.data.InterestRate[params.duration])

        PremiumTotal.value += (PremiumTotal.value*abs(params.price - self.data.CallOption[params.address].strikePrice))/(params.price)
        
        PaidAmount = sp.local('PaidAmount', self.data.CallOption[params.address].premium)

        self.data.CallOption[params.address].premium = PremiumTotal.value

        PremiumTotal.value += self.data.CallOption[params.address].options*abs(10000)

        self.data.adminAccount += self.data.CallOption[params.address].options*9*1000
        self.data.CallOption[params.address].reward = self.data.CallOption[params.address].options*1000

        sp.verify(TotalAvailable.value >= TotalAmount.value, message = "Insufficient Funds to cover up Order Amount")
        sp.verify(PaidAmount.value  >= PremiumTotal.value, message= "Premium is underpaid for the CALL Option contract")

        self.data.LockedSupply = self.data.LockedSupply + TotalAmount.value

        sp.verify(self.data.LockedSupply*10 <= self.data.totalSupply*9, message="Options utilizes more than 90 percent of the pool's funds.")
        
        

    @sp.entry_point
    def ExerciseCallOption(self,params):

        sp.verify(self.data.CallOption.contains(sp.sender), message = "Sender has not purchased Call Option")
        sp.verify(sp.now <= self.data.CallOption[sp.sender].expiry, message = "PUT Options have already expired")

        # Call Oracle to Fetch Price 
        call = sp.contract(sp.TRecord(owner = sp.TAddress),sp.address("KT1TeegbL5HrPqHivCq7Cg4Ph4y1TciFEHTm"), entry_point = "SecuritiesExercise").open_some(message = "Oracle Call failed")
        calldata = sp.record(owner = sp.sender)
        sp.transfer(calldata, sp.mutez(0), call)

    @sp.entry_point
    def OracleExerciseSecurity(self,params):
        
        sp.set_type(params, sp.TRecord(price = sp.TNat, owner = sp.TAddress))

        sp.verify(sp.sender == sp.address("KT1TeegbL5HrPqHivCq7Cg4Ph4y1TciFEHTm"), message = "Sender isn't Oracle Contract")
        sp.verify(self.data.CallOption[params.owner].strikePrice < params.price, message = "Current Price is less than or equal to Strike Price")

        sp.if self.data.CallOption[params.owner].strikePrice < params.price:
            
            TotalAmount = sp.local('TotalAmount',self.data.CallOption[params.owner].options*abs(1000000))
            
            AmountLeft = sp.local('Amount',self.data.CallOption[params.owner].strikePrice*1000000*self.data.CallOption[params.owner].options)
            AmountLeft.value = AmountLeft.value/params.price

            self.data.WithdrawFund += self.data.CallOption[params.owner].premium
            self.data.WithdrawFund += self.data.CallOption[params.owner].reward

            self.data.LockedSupply = abs(self.data.LockedSupply - TotalAmount.value)
            self.data.totalSupply = abs(self.data.totalSupply - abs(TotalAmount.value - AmountLeft.value)) 
            
            ProfitValue = sp.local('ProfitValue',abs(TotalAmount.value - AmountLeft.value))
            
            sp.send(params.owner,sp.mutez(ProfitValue.value))

            del self.data.CallOption[params.owner]
    
    @sp.entry_point
    def FreeSecurity(self,params):

        sp.set_type(params, sp.TRecord(address = sp.TAddress))

        sp.verify(self.data.CallOption.contains(params.address), message = "Order with such address does not exist.")
        
        sp.if sp.now > self.data.CallOption[params.address].expiry :
        
            TotalAmount = sp.local('TotalAmount',self.data.CallOption[params.address].options*1000000)
    
            self.data.LockedSupply = abs(self.data.LockedSupply - TotalAmount.value)
            self.data.WithdrawFund += self.data.CallOption[params.address].premium

            TransferAmount = sp.local("TransferAmount",self.data.CallOption[params.address].reward)
            sp.send(sp.sender,sp.mutez(TransferAmount.value))

            del self.data.CallOption[params.address]

    @sp.entry_point 
    def ContractWriterMint(self,params):

        sp.set_type(params, sp.TRecord(amount = sp.TNat))

        sp.verify(sp.amount == sp.mutez(params.amount))

        MintAmount = sp.local('MintAmount',sp.nat(0))

        sp.if self.data.tokenMinted == sp.nat(0):

            MintAmount.value = params.amount
            self.data.tokenMinted = params.amount

        sp.else:  

            MintAmount.value = params.amount * self.data.tokenMinted
            MintAmount.value = MintAmount.value/(self.data.totalSupply + self.data.WithdrawFund)
            self.data.tokenMinted += MintAmount.value

        self.data.totalSupply = sp.fst(sp.ediv(sp.balance , sp.mutez(1)).open_some( message = "unable to convert balance to nat value"))

        mint = sp.contract(sp.TRecord(value = sp.TNat , address = sp.TAddress), sp.address("KT19qoEwvhrH7XnFkbhJnKCr33ywomStTt2g"), entry_point = "mint").open_some(message = "minting wDAL call failed")
        mintdata = sp.record(value = MintAmount.value , address = sp.sender)
        sp.transfer(mintdata, sp.mutez(0), mint)
        

    @sp.entry_point 
    def ContractWriterBurn(self,params):
        
        sp.set_type(params, sp.TRecord(amount = sp.TNat))

        sp.verify(self.data.tokenMinted >= params.amount, message = "Burn Amount is greater than Total Tokens minted")
        
        TransferAmount = sp.local('TransferAmount',params.amount*(self.data.totalSupply + self.data.WithdrawFund))
        TransferAmount.value = TransferAmount.value/self.data.tokenMinted

        FreeAmount = sp.local('FreeAmount',abs((self.data.totalSupply + self.data.WithdrawFund) - self.data.LockedSupply))
        
        sp.if FreeAmount.value >= TransferAmount.value:

            self.data.tokenMinted = abs(self.data.tokenMinted - params.amount)

            # Integrate Withdrawl Fund into Withdraw 
            sp.if self.data.WithdrawFund >= TransferAmount.value:
                self.data.WithdrawFund = abs(self.data.WithdrawFund - TransferAmount.value)

            sp.else: 

                AmountLeft = sp.local('AmountLeft',abs(TransferAmount.value - self.data.WithdrawFund))
                self.data.totalSupply = abs(self.data.totalSupply - AmountLeft.value)
                self.data.WithdrawFund = 0 
            
            # Add Burn Token Call First 

            burn = sp.contract(sp.TRecord(value = sp.TNat , address = sp.TAddress), sp.address("KT19qoEwvhrH7XnFkbhJnKCr33ywomStTt2g"), entry_point = "burn").open_some(message = "burning wDAL call failed")
            burndata = sp.record(value = params.amount , address = sp.sender)
            sp.transfer(burndata, sp.mutez(0), burn)

            # Transfering XTZ 
            sp.send(sp.sender,sp.mutez(TransferAmount.value))
            

    @sp.entry_point
    def ChangeState(self,params):

        sp.verify(sp.sender == self.data.administrator, message = "User not authorized to Change State of contract")
        self.data.paused = ~self.data.paused
    
    @sp.entry_point
    def UpdatePremium(self,params):
        sp.set_type(params, sp.TRecord(one = sp.TNat, two = sp.TNat, three = sp.TNat,four = sp.TNat ))

        sp.verify(sp.sender == self.data.administrator, message = "User not authorized to Update Premiums")
        
        self.data.InterestRate[1] = params.one
        self.data.InterestRate[7] = params.two 
        self.data.InterestRate[14] = params.three
        self.data.InterestRate[21] = params.four

    @sp.entry_point
    def AdminWithdraw(self,params):
        
        sp.verify(sp.sender == self.data.administrator , message = "User not authorized to withdraw admin funds.")

        sp.verify(self.data.adminAccount > 0 , message = " No funds available to transfer")
        PaymentAmount = sp.local('PaymentAmount',self.data.adminAccount)

        sp.send(self.data.administrator,sp.mutez(PaymentAmount.value))
        self.data.adminAccount = 0

if "templates" not in __name__:
    @sp.add_test(name = "Call Options Contract")
    def test():

        scenario = sp.test_scenario()

        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.test_account("Admin")
        
        alice = sp.test_account("Alice")
        bob   = sp.test_account("Bob")
        robert = sp.test_account("Robert")

        scenario.h1("Contract")

        oracle  = USDOracle(sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))
        scenario += oracle 
  
        options = Securities(sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))
        scenario += options
        
        scenario += oracle.feedData(price=400).run(sender=sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))
        
        scenario += oracle.changeSecurities(address=options.address).run(sender=sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))

        scenario += options.ContractWriterMint(amount=2000000).run(sender=alice, amount = sp.tez(2))
        # scenario += options.ContractWriterBurn(amount=1000000).run(sender=alice)
        scenario += options.ContractWriterMint(amount=10000000).run(sender=robert,amount = sp.tez(10))

        # scenario += options.ContractWriterBurn(amount=100000000000000000000).run(sender=robert)
        scenario += options.PurchaseCallOption(price=400, duration = 1 , amount = 1000000, order = 10).run(sender = bob,amount =sp.tez(1))
        
        scenario += oracle.feedData(price=600).run(sender=sp.address("tz1YCDdMbSB3HVbmiEHh1hnERBdoxZNdAUAF"))
        
        scenario += options.ExerciseCallOption().run(sender = bob)
        # scenario += oracle.SecuritiesExercise(owner = bob.address).run(sender = bob )