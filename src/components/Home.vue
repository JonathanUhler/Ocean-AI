<template>
  <div id="Header">
	<div id="Title"><b><span class="oceanai">ocean</span>.ai</b></div>
	<VButton x="70%" y="30%" c="blue" o t="About" scroll s="small" L="#scrollto"></VButton>
	<VButton x="90%" y="30%" c="blue"  t="Map" s="small"  L="map"></VButton>
	<VButton x="80%" y="30%" c="blue" o t="Cause" s="small" scroll L="#scrollto2"></VButton>
  </div>
  <img id="Image" src="../assets/beach2.png">
  
  <div id="Pitch"><b>There are over<br><span class="trillion">5 TRILLION</span></b></div>
  <span class="trash"> <b>pieces of trash in the <span class="oceanai">ocean.</span></b></span>
  <div id="SubPitch">It's time to use AI to help fix that.</div>
  <VButton x="23%" y="65%" c="blue" t="Explore" s="medium" L="map"></VButton>
 <div id="scrollto"></div>
 <div id="scrollto2"></div>
  <div class="ocean">
  <div class="wave"></div>
  <div class="wave"></div>
 
  <VFeature y="0px" c="rgb(245,245,245)" side="left" mp="The Ocean is Full of Trash" sp="There are thousands of heaps of trash in the ocean, scatttered all throughout the globe. Most of them are far from land and drift constantly, which makes it near impossible to clean them up." i="planet2.png" iw="28%" ih="500px" iy="70px"></VFeature>
  <VFeature y="500px" c="rgb(245,245,245)" side="right" mp="AI is Changing the Game" sp="With new advanced AI data analysis of wind and ocean currents, we can not only map all of these heaps but also predict where they'll drift to next, which facilitates the clean up process." i="data.png" iw="25%" ih="440px" iy="70px" ix="19%"></VFeature>
  <VFeature y="1000px" c="rgb(245,245,245)" side="left" mp="The Trash Map" sp="Our map shows trash heaps around the world with detailed information, and uses data to predict where they'll be in a week or a month." i="map.webp" iw="23%" ih="300px" iy="120px"></VFeature>
  <VFeature y="1500px" c="rgb(245,245,245)" side="right" mp="Purifying for a Better Future" sp="This allows clean up efforts to better locate trash heaps and clean them up. We need to purify the ocean not just for humans, but for all living organisms on Earth." i="ocean2.png" iw="25%" ih="450px" iy="60px" ix="19%"></VFeature>
	<img id="FinalImage" src="../assets/o.png">
	<div id="FinalPitch">It's time we used modern technology to solve environmental problems. Our Earth depends on it!</div>
	<VButton x="42%" y="2500px" c="blue" t="Explore" s="large" L="map"></VButton>
</div>
</template>

<script>
import VButton from "./VButton.vue";
import VFeature from "./VFeature.vue";
export default {
  name: 'Home',
  components:{
	VButton,
	VFeature
	},
	methods:{
		scroll(){
			var container = this.$el.querySelector("#scrollto");
			container.scrollTop = container.scrollHeight;
		},
		countDown(){
			console.log(window.scrollY);
			if(window.scrollY<=700){
				document.getElementsByClassName("ii")[0].style.transform="scale(1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1)";
			}
			else if(window.scrollY>=700 && window.scrollY<=1200){
				document.getElementsByClassName("ii")[0].style.transform="scale(1.1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1)";
			}
			else if(window.scrollY>=1200 && window.scrollY<=1700){
				document.getElementsByClassName("ii")[0].style.transform="scale(1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1.1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1)";
			}
			else if(window.scrollY>=1700 && window.scrollY<=2200){
				document.getElementsByClassName("ii")[0].style.transform="scale(1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1.1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1)";
			}
			else if(window.scrollY>=2200 && window.scrollY<=2700){
				document.getElementsByClassName("ii")[0].style.transform="scale(1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1.1)";
			}
			else if(window.scrollY>=2700){
				document.getElementsByClassName("ii")[0].style.transform="scale(1)";
				document.getElementsByClassName("ii")[1].style.transform="scale(1)";
				document.getElementsByClassName("ii")[2].style.transform="scale(1)";
				document.getElementsByClassName("ii")[3].style.transform="scale(1)";
			}
		}
	},
	mounted(){
		this.$nextTick(function () {
            window.setInterval(() => {
                this.countDown();
            },10);
        })
	}
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
body{
	font-family: 'Open Sans', sans-serif;
	background-color:rgb(245,245,245);
	height:3700px;
	//background:radial-gradient(ellipse at center, rgba(255,254,234,1) 0%, rgba(255,254,234,1) 35%, #B7E8EB 100%);
  overflow-x:hidden;
}
html {
  scroll-behavior: smooth;
}

#Header{
	position:absolute;
	width:100%;
	height:10%;
	left:0%;
	top:0%;
}
#Title{
	width:10%;
	position:absolute;
	height:100%;
	left:1%;
	top:20%;
	text-align:center;
	display:flex;
	justify-content:center;
	font-size:40px;
}
.ocean { 
  height: 5%;
  width:100%;
  position:absolute;
  bottom:-50px;
  left:0;
  background: #015871;
}

.wave {
  background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/85486/wave.svg) repeat-x; 
  position: absolute;
  top: -198px;
  width: 6400px;
  height: 198px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) infinite;
  transform: translate3d(0, 0, 0);
}

.wave:nth-of-type(2) {
  top: -175px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) -.125s infinite, swell 7s ease -1.25s infinite;
  opacity: 1;
}

@keyframes wave {
  0% {
    margin-left: 0;
  }
  100% {
    margin-left: -1600px;
  }
}

@keyframes swell {
  0%, 100% {
    transform: translate3d(0,-25px,0);
  }
  50% {
    transform: translate3d(0,5px,0);
  }
}
	
	
	
#Image{
	position:absolute;
	width:700px;
	height:600px;
	left:50%;
	top:10%;
	animation-name: floating;
    animation-duration: 3s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
}
@keyframes floating {
    0% { transform: translate(0,  0px); }
    50%  { transform: translate(0px, 25px); }
    100%   { transform: translate(-0, -0px); }   
}
#FinalImage{
	position:absolute;
	width:400px;
	height:400px;
	left:30%;
	top:2050px;
	
}
#Pitch{
	position:absolute;
	color:rgb(70,70,70);
	width:50%;
	height:20%;
	left:5%;
	top:25%;
	font-size:75px;
	text-align:center;
	display:flex;
	justify-content:center;
	align-items:center;
	line-height:98px;
}
#SubPitch{
	position:absolute;
	color:rgb(70,70,70);
	width:50%;
	height:20%;
	left:5%;
	top:47%;
	font-size:30px;
	text-align:center;
	display:flex;
	justify-content:center;
	align-items:center;
}
.trillion{
	font-size:100px;
background: #E00000;
background: radial-gradient(circle farthest-corner at center center, #E00000 0%, #E84141 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
.trash{
	font-size:39px;
	position:absolute;
	width:50%;
	height:20%;
	left:5%;
	top:45%;
	text-align:center;
}

#FinalPitch{
	position:absolute;
	color:rgb(70,70,70);
	width:30%;
	height:20%;
	left:55%;
	top:2250px;
	font-size:30px;
	text-align:left;
	display:flex;
	justify-content:center;
	align-items:center;
}
.oceanai{
	background: #004BE0;
background: radial-gradient(circle farthest-corner at center center, #004BE0 0%, #0C90E8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
a{
	position:absolute;
	left:10%;
	top:30%;
	width:100px;
	height:100px;
}
#scrollto{
	position:absolute;
	top:210%;
}
#scrollto2{
	position:absolute;
	top:110%;
}

</style>
