<template>
  <div >
    
    <link href="https://fonts.googleapis.com/css?family=Work+Sans:100,200,300,400,500,600,700,800,900" rel="stylesheet"/>
	  <link href="https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet"/>
	  <link href="https://fonts.googleapis.com/css?family=Crimson+Text:400,400i,600,600i,700,700i" rel="stylesheet"/>	



    <link rel="stylesheet" href="/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="/css/owl.carousel.css"/>
    <link rel="stylesheet" href="/css/owl.transitions.css"/>
    <link rel="stylesheet" href="/css/style.css"/>
    <link rel="stylesheet" href="/css/colors/color-green.css"/>

    <div class="loader green">
		<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
		 width="24px" height="30px" viewBox="0 0 24 30" style="enable-background:new 0 0 50 50;" xml:space="preserve">
			<rect x="0" y="0" width="4" height="10" fill="#333">
				<animateTransform attributeType="xml"
				attributeName="transform" type="translate"
				values="0 0; 0 20; 0 0"
				begin="0" dur="0.6s" repeatCount="indefinite" />
			</rect>
			<rect x="10" y="0" width="4" height="10" fill="#333">
				<animateTransform attributeType="xml"
				attributeName="transform" type="translate"
				values="0 0; 0 20; 0 0"
				begin="0.2s" dur="0.6s" repeatCount="indefinite" />
			</rect>
			<rect x="20" y="0" width="4" height="10" fill="#333">
				<animateTransform attributeType="xml"
				attributeName="transform" type="translate"
				values="0 0; 0 20; 0 0"
				begin="0.4s" dur="0.6s" repeatCount="indefinite" />
			</rect>
		</svg>	
	</div>

  <!-- Nav and Logo
	================================================== -->
	
	<div id="menu-wrap" class="menu-back cbp-af-header dark">
		<div class="container">
			<div class="row">
				<div class="col-12">
					<nav class="navbar navbar-expand-lg navbar-light bg-light mx-lg-0">
						<a class="navbar-brand" href="/">Decentralized Derivatives</a>
						<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
							<span class="navbar-toggler-icon">
								<span class="menu-icon__line menu-icon__line-left"></span>
								<span class="menu-icon__line"></span>
								<span class="menu-icon__line menu-icon__line-right"></span>
							</span>
						</button>

						<div class="collapse navbar-collapse" id="navbarSupportedContent">
							<ul class="navbar-nav ml-auto">
								<li class="nav-item">
									<a class="nav-link" href="#concept">Concept</a>
								</li>
								<li class="nav-item">
									<a class="nav-link" href="#roadmap">Roadmap</a>
								</li>
								<li class="nav-item">
									<a class="nav-link" href="#faq">FAQ</a>
								</li>
								<li class="nav-item mt-2">
									<a class="btn btn-primary js-tilt" href="#app" role="button" data-tilt-perspective="300" data-tilt-speed="700" data-tilt-max="24"><span>Call Options</span></a>
								</li>
							</ul>
						</div>
					</nav>				
				</div>
			</div>
		</div>
	</div>

	<div class="section full-height height-auto-lg hide-over background-light-blue-2 background-image-cover" style="background-image: url('img/background.png');">
		<div class="hero-center-wrap relative-on-lg">
			<div class="container">
				<div class="row">
					<div class="col-lg-5 text-center text-lg-left align-self-center z-bigger">
						<h2 class="text-white">The time of great changes.</h2>
						<p class="mt-3 mb-4 pb-3 font-weight-normal text-white">We’ve built companies from the ground up.</p>
						<a class="btn btn-primary mx-0 js-tilt" href="#" role="button" data-tilt-perspective="300" data-tilt-speed="700" data-tilt-max="24"><span>Use Algorithm </span></a>
					</div>
					<div class="col-lg-7 mt-5 mt-lg-0">
						<div class="img-wrap">
							<img src="img/cripto.svg" alt="">
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="ocean blue">
			<div class="wave"></div>
			<div class="wave"></div>
		</div>
		<div id="particles-js" class="min-height-snd"></div>
	</div>


	<div class="section padding-top-big background-gradient-light-re" id="concept">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<div class="title-wrap text-center">
						<div class="back-title strong">concept</div>
						<h3 class="text-white">We are the only global<br>mining operation.</h3>
						<p class="color-pr">Lend your digital assets to others for trading and earn an interest through margin trading loans.</p>
					</div>
				</div>
				<div class="col-md-4" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.3s">
					<div class="concept-box">
						<img class="mb-4" src="img/con-1.svg" alt="">
						<h5 class="text-white">Independent</h5>
						<p class="text-grey">Our mobility concept enables super-simple transportation and worldwide deployment.</p>
					</div>
				</div>
				<div class="col-md-4 mt-4 mt-md-0" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.5s">
					<div class="concept-box">
						<img class="mb-4" src="img/con-2.svg" alt="">
						<h5 class="text-white">Fully Scalable</h5>
						<p class="text-grey">Mobile and efficient low-cost hardware and optimized propietary management.</p>
					</div>
				</div>
				<div class="col-md-4 mt-4 mt-md-0" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.7s">
					<div class="concept-box">
						<img class="mb-4" src="img/con-3.svg" alt="">
						<h5 class="text-white">High Growth</h5>
						<p class="text-grey">Our reinvestment strategy enables us to quickly grow our fleet of mobile units.</p>
					</div>
				</div>
				<div class="col-md-12 padding-top-bottom" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.3s">
					<div class="line-sep"></div>
				</div>
			</div>	
		</div>
		<div class="section background-image-cover" style="background-image: url('img/background-1.png');">
			<div class="container">
				<div class="row">
					<div class="col-md-6 align-self-center" data-scroll-reveal="enter left move 50px over 0.6s after 0.3s">
						<h4 class="text-white">Creating a win-win<br>for everyone</h4>
						<p class="lead text-grey">An exciting business opportunity should come with equally exciting rewards.</p>
						<p class="text-grey">Early adopters can earn up to a 200% bonus based on the final token value should we reach our 100 mil tokens hardcap during our planned token sale event.</p>
						<a class="btn btn-primary mt-4 mx-0 js-tilt" href="#roadmap" data-gal="m_PageScroll2id" data-ps2id-offset="68" role="button" data-tilt-perspective="300" data-tilt-speed="700" data-tilt-max="24"><span>Roadmap</span></a>
					</div>
					<div class="col-md-5 offset-md-1 order-first order-md-last mb-4 mb-md-0">
						<div class="img-wrap">
							<img src="img/1.png" alt="">
						</div>
					</div>
				</div>	
			</div>	
			<div class="container">
				<div class="row">
					<div class="col-md-12 my-4"></div>
				</div>	
			</div>
			<div class="container">
				<div class="row">
					<div class="col-md-5 mb-4 mb-md-0">
						<div class="img-wrap">
							<img src="img/2.png" alt="">
						</div>
					</div>
					<div class="col-md-6 offset-md-1 align-self-center" data-scroll-reveal="enter right move 50px over 0.6s after 0.3s">
						<h4 class="text-white">More than just a price jump</h4>
						<p class="text-grey">The Coeus token sale events are unique as they offer tiered bonuses which include not only an increasing token price but also lifetime discounts, a commitment from us to support our tokens liquidity and future value, as well as access to future pre-pre-Token sale events.</p>
						<a class="btn btn-primary mt-4 mx-0 js-tilt" href="#buy" data-gal="m_PageScroll2id" data-ps2id-offset="120" role="button" data-tilt-perspective="300" data-tilt-speed="700" data-tilt-max="24"><span>Buy Tokens</span></a>
					</div>
				</div>	
			</div>	
		</div>	
	</div>

	<div class="section padding-top-big pb-4 background-gradient-light" id="roadmap">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<div class="title-wrap text-center">
						<div class="back-title strong">roadmap</div>
						<h3 class="text-white">Making the most<br>out of unused.</h3>
						<p class="color-pr">The Coeus token sale events are unique as they offer tiered bonuses which include increasing token price and lifetime discounts.</p>
					</div>
				</div>
				<div class="col-md-12">
					<div class="customNavigation">
						<a class="prev-roadmap dark"><i class="fa fa-angle-left"></i></a>
						<a class="next-roadmap dark"><i class="fa fa-angle-right"></i></a>
					</div>
					<div id="owl-roadmap" class="owl-carousel owl-theme">											
						<div class="item blue">						 
							<div class="roadmap-box background-light-blue-2">
								<p class="mb-4 achieved"><span>Achieved</span></p>
								<h6 class="text-white">March 2021.</h6>
								<p class="text-grey">Start of Development</p>
							</div>	
						</div>											
						<div class="item blue"> 						 
							<div class="roadmap-box current-road background-light-blue-2 roadmap-shadow">
								<p class="mb-4"><span>Current</span></p>
								<h6 class="text-white">Apr 2021.</h6>
								<p class="text-grey">Writing Routing Algorithm</p>
							</div>	
						</div>												
						<div class="item blue"> 						 
							<div class="roadmap-box next-road background-light-blue-2">
								<p class="mb-4 plan"><span>Plan</span></p>
								<h6 class="text-white">May 2021.</h6>
								<p class="text-grey">Report Writing</p>
							</div>	
						</div>											
						<div class="item blue"> 						 
							<div class="roadmap-box next-road background-light-blue-2">
								<p class="mb-4 plan"><span>Plan</span></p>
								<h6 class="text-white">May 2021</h6>
								<p class="text-grey">Deployment </p>
							</div>	
						</div>																						
						<div class="item blue"> 						 
							<div class="roadmap-box next-road background-light-blue-2">
								<p class="mb-4 plan"><span>Plan</span></p>
								<h6 class="text-white">July 2021</h6>
								<p class="text-grey">Research For Future</p>
							</div>	
						</div>							
					</div>
				</div>
			</div>	
		</div>
	
	</div>
	
	<div class="section padding-top-big pb-4  background-gradient-light-re" id="faq">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<div class="title-wrap text-center">
						<div class="back-title strong">faq</div>
						<h3 class="text-white">Questions and Answers</h3>
						<p class="color-pr">Listed questions and answers, all supposed to be commonly asked in some context, and pertaining to a particular topic.</p>
					</div>
				</div>
			</div>	
		</div>
		<div class="container">
			<div class="row">
				<div class="col-md-6" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.3s">
					<div id="accordion" class="accordion-style">
						<div class="card">
							<div class="card-header" id="headingOne">
								<a class="text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
									What exactly is your token?
								</a>
							</div>

							<div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
								<div class="card-body">
									<h6 class="text-white">What exactly is your token?</h6>
									<p class="text-grey">Token is a community of people who want to mine cryptocurrency profitably by combining resources to achieve savings on equipment and ultra-low-cost electricity.</p>
								</div>
							</div>
						</div>
						
						<div class="card">
							<div class="card-header" id="headingTwo">
								<a class="collapsed text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
									What’s your overall strategy?
								</a>
							</div>
							<div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
								<div class="card-body">
									<h6 class="text-white">What’s your overall strategy?</h6>
									<p class="text-grey">Our strategy is very straightforward: 1) raise funds, 2) leverage those funds to procure the best mining equipment and other necessities at the lowest possible prices, 3) set up the hardware in a suitable facility; 4) start mining; 5) distribute what we mine.</p>
								</div>
							</div>
						</div>
						
						<div class="card">
							<div class="card-header" id="headingThree">
								<a class="collapsed text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
									What is bitcoin?
								</a>
							</div>
							<div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
								<div class="card-body">
									<h6 class="text-white">What is bitcoin?</h6>
									<p class="text-grey">Bitcoin is a cryptocurrency and worldwide payment system. It is the first decentralised digital currency, as the system works without a central bank or single administrator.</p>
								</div>
							</div>
						</div>
					</div>				
				</div>
				<div class="col-md-6 mt-4 mt-md-0" data-scroll-reveal="enter bottom move 50px over 0.6s after 0.5s">
					<div id="accordion-snd" class="accordion-style">
						<div class="card">
							<div class="card-header" id="headingFour">
								<a class="text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseFour" aria-expanded="true" aria-controls="collapseFour">
									What is blockchain?
								</a>
							</div>

							<div id="collapseFour" class="collapse show" aria-labelledby="headingFour" data-parent="#accordion-snd">
								<div class="card-body">
									<h6 class="text-white">What is blockchain?</h6>
									<p class="text-grey">A blockchain is the technology on which cryptocurrency is based. A blockchain is basically a continuously growing list of records called blocks that are linked and secured using cryptography. </p>
								</div>
							</div>
						</div>
						
						<div class="card">
							<div class="card-header" id="headingFive">
								<a class="collapsed text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
									What is cryptocurrency?
								</a>
							</div>
							<div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordion-snd">
								<div class="card-body">
									<h6 class="text-white">What is cryptocurrency?</h6>
									<p class="text-grey">A cryptocurrency is a digital asset designed to work as a medium of exchange that uses cryptography to secure its transactions, to control the creation of additional units, and to verify the transfer of assets.</p>
								</div>
							</div>
						</div>
						
						<div class="card">
							<div class="card-header" id="headingSix">
								<a class="collapsed text-white background-light-blue-2" data-toggle="collapse" data-target="#collapseSix" aria-expanded="false" aria-controls="collapseSix">
									How much should I invest?
								</a>
							</div>
							<div id="collapseSix" class="collapse" aria-labelledby="headingSix" data-parent="#accordion-snd">
								<div class="card-body">
									<h6 class="text-white">How much should I invest?</h6>
									<p class="text-grey">Cryptocurrency mining is not without risk, and we are open and candid about those risks in our White Paper.</p>
								</div>
							</div>
						</div>
					</div>				
				</div>
			</div>	
		</div>
	</div>
	
	
	
	<div class="scroll-to-top light">to top</div>
  <script src="/js/jquery-3.2.1.min.js"></script>
	<script src="/js/popper.min.js"></script> 
	<script src="/js/bootstrap.min.js"></script>
	<script src="/js/plugins.js"></script> 
	<script src="/js/particles.js"></script> 
	<script src="/js/custom-azure.js"></script>  

  </div>
</template>

<script>

export default {
  
}
</script>

