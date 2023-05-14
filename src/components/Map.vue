<template>
	<div id="Background" @mousedown="mouseDown" @mouseup="mouseUp">
	<img :style="css" id="my-image" :src="require(`../assets/world3.svg`)" />
	</div>
	
	<VButton x="1.5%" y="2%" t="Back" c="blue" s="small" L="/"></VButton>
	<div id="infofake">
			<div id="numfake">✔️</div>
			<div id="id"><b>Click a Red Dot to Begin</b></div>
		</div>
	<div v-for="(trash,index) in activeDots">
		<Trash  :x="trash.x" :y="trash.y" :x7="trash.x7" :y7="trash.y7" :s="trash.s" :n="trash.n" :lat="trash.lat" :log="trash.lon" :id="trash.id" :nu="index"></Trash>
	</div>
	<VInput x="1%" y="93%" c="blue" s="medium" t="Search ID:"></VInput>
	<div class="slidecontainer">
		<div id="slidelabel">Minimum Size</div>
		
		<input id="slide" type="range" v-model="minSize">
		<div id="slidemin">1</div>
		<div id="slidemax">100</div>
	</div>
</template>
<script>
import Trash from "./Trash.vue";
import VButton from "./VButton.vue";
import VInput from "./VInput.vue";
export default{
	components:{
		Trash,
		VButton,
		VInput,
	},
	data(){
		return{
			trashes:[{id:"250207",n:"26",lat:"-40.2298",lon:"-57.9988",x:"610px",y:"650px",x7:"620px",y7:"655px",s:"13px"},{id:"601530",n:"16",lat:"-39.1952",lon:"-59.5777",x:"600px",y:"645px",x7:"635px",y7:"650px",s:"8px"},{id:"627284",n:"46",lat:"-32.3842",lon:"-61.1024",x:"590px",y:"610px",x7:"560px",y7:"605px",s:"23px"},{id:"470478",n:"16",lat:"-27.0774",lon:"-62.6056",x:"585px",y:"585px",x7:"600px",y7:"560px",s:"8px"},{id:"006432",n:"77",lat:"-24.3969",lon:"-69.5591",x:"550px",y:"570px",x7:"620px",y7:"550px",s:"38px"},{id:"673538",n:"25",lat:"-22.5053",lon:"-71.4723",x:"540px",y:"560px",x7:"505px",y7:"540px",s:"12px"},{id:"410427",n:"18",lat:"-17.0959",lon:"-78.9114",x:"505px",y:"535px",x7:"475px",y7:"515px",s:"9px"},{id:"418029",n:"64",lat:"-12.8764",lon:"-84.1094",x:"475px",y:"510px",x7:"345px",y7:"495px",s:"32px"},{id:"181703",n:"77",lat:"-7.8696",lon:"-87.4908",x:"460px",y:"485px",x7:"475px",y7:"470px",s:"38px"},{id:"245745",n:"29",lat:"-0.7149",lon:"-86.6081",x:"465px",y:"450px",x7:"470px",y7:"435px",s:"14px"},{id:"612391",n:"19",lat:"5.0173",lon:"-88.4567",x:"455px",y:"420px",x7:"440px",y7:"400px",s:"9px"},{id:"737775",n:"19",lat:"8.6541",lon:"-92.7155",x:"435px",y:"405px",x7:"450px",y7:"380px",s:"9px"},{id:"909063",n:"27",lat:"14.2671",lon:"-101.1353",x:"390px",y:"375px",x7:"395px",y7:"370px",s:"13px"},{id:"647257",n:"53",lat:"20.1086",lon:"-105.1995",x:"370px",y:"345px",x7:"360px",y7:"330px",s:"26px"},{id:"916733",n:"16",lat:"17.4025",lon:"-97.0723",x:"410px",y:"360px",x7:"445px",y7:"350px",s:"8px"},{id:"188179",n:"27",lat:"5.7838",lon:"-70.4181",x:"545px",y:"420px",x7:"470px",y7:"405px",s:"13px"},{id:"664098",n:"17",lat:"-13.7892",lon:"-62.2287",x:"585px",y:"515px",x7:"575px",y7:"500px",s:"8px"},{id:"199873",n:"27",lat:"-24.1088",lon:"-54.7512",x:"625px",y:"570px",x7:"630px",y7:"555px",s:"13px"},{id:"724115",n:"20",lat:"13.3166",lon:"-74.8651",x:"525px",y:"380px",x7:"505px",y7:"375px",s:"10px"},{id:"134519",n:"25",lat:"17.8524",lon:"-66.5664",x:"565px",y:"360px",x7:"575px",y7:"355px",s:"12px"},{id:"052016",n:"22",lat:"16.5501",lon:"-76.6176",x:"515px",y:"365px",x7:"1795px",y7:"355px",s:"11px"},{id:"035131",n:"23",lat:"32.1110",lon:"-50.4470",x:"645px",y:"285px",x7:"1010px",y7:"295px",s:"11px"},{id:"804451",n:"37",lat:"12.9336",lon:"-60.1149",x:"595px",y:"385px",x7:"605px",y7:"365px",s:"18px"},{id:"444717",n:"24",lat:"26.7559",lon:"-75.1804",x:"520px",y:"315px",x7:"515px",y7:"320px",s:"12px"},{id:"247255",n:"24",lat:"32.2500",lon:"-81.0713",x:"490px",y:"285px",x7:"505px",y7:"290px",s:"12px"},{id:"502134",n:"96",lat:"40.9310",lon:"-76.7829",x:"515px",y:"245px",x7:"510px",y7:"260px",s:"48px"},{id:"290740",n:"17",lat:"47.2036",lon:"-64.4868",x:"575px",y:"210px",x7:"585px",y7:"230px",s:"8px"},{id:"600725",n:"22",lat:"55.1655",lon:"-53.4817",x:"630px",y:"170px",x7:"705px",y7:"170px",s:"11px"},{id:"346129",n:"81",lat:"-5.1288",lon:"52.2267",x:"1160px",y:"475px",x7:"1210px",y7:"460px",s:"40px"},{id:"008596",n:"24",lat:"-8.0474",lon:"48.4209",x:"1140px",y:"490px",x7:"1300px",y7:"470px",s:"12px"},{id:"316907",n:"88",lat:"-16.1939",lon:"48.7995",x:"1140px",y:"530px",x7:"1170px",y7:"520px",s:"44px"},{id:"880033",n:"89",lat:"-16.0609",lon:"59.6447",x:"1195px",y:"530px",x7:"990px",y7:"525px",s:"44px"},{id:"080181",n:"39",lat:"-30.7108",lon:"56.6478",x:"1180px",y:"600px",x7:"1165px",y7:"605px",s:"19px"},{id:"954382",n:"23",lat:"-13.2972",lon:"56.9362",x:"1180px",y:"515px",x7:"1015px",y7:"505px",s:"11px"},{id:"354733",n:"26",lat:"-26.0855",lon:"50.5844",x:"1150px",y:"580px",x7:"1140px",y7:"580px",s:"13px"},{id:"029446",n:"19",lat:"-11.0234",lon:"43.6329",x:"1115px",y:"505px",x7:"1150px",y7:"490px",s:"9px"},{id:"022233",n:"19",lat:"-31.7290",lon:"56.5697",x:"1180px",y:"605px",x7:"1170px",y7:"610px",s:"9px"},{id:"256304",n:"29",lat:"-43.3907",lon:"59.6604",x:"1195px",y:"665px",x7:"1155px",y7:"665px",s:"14px"},{id:"838673",n:"21",lat:"-39.9909",lon:"50.1711",x:"1150px",y:"645px",x7:"1155px",y7:"650px",s:"10px"},{id:"636783",n:"28",lat:"-43.0975",lon:"50.0125",x:"1150px",y:"665px",x7:"1160px",y7:"665px",s:"14px"},{id:"836505",n:"95",lat:"-33.8126",lon:"36.3291",x:"1080px",y:"615px",x7:"1045px",y7:"620px",s:"47px"},{id:"305057",n:"27",lat:"-30.9162",lon:"29.7004",x:"1045px",y:"600px",x7:"1055px",y7:"605px",s:"13px"},{id:"971643",n:"25",lat:"-48.2050",lon:"71.4805",x:"1255px",y:"690px",x7:"1290px",y7:"690px",s:"12px"},{id:"039731",n:"28",lat:"-61.9129",lon:"68.1693",x:"1240px",y:"755px",x7:"1190px",y7:"740px",s:"14px"},{id:"081429",n:"42",lat:"-68.5368",lon:"50.5676",x:"1150px",y:"790px",x7:"1155px",y7:"795px",s:"21px"},{id:"065726",n:"25",lat:"-78.2203",lon:"22.7247",x:"1010px",y:"840px",x7:"955px",y7:"840px",s:"12px"},{id:"175782",n:"59",lat:"-81.7098",lon:"42.0969",x:"1110px",y:"855px",x7:"1105px",y7:"860px",s:"29px"},{id:"540690",n:"20",lat:"-79.0891",lon:"72.0733",x:"1260px",y:"845px",x7:"1260px",y7:"825px",s:"10px"},{id:"126902",n:"26",lat:"-90.4797",lon:"69.7207",x:"1245px",y:"900px",x7:"1245px",y7:"880px",s:"13px"},{id:"955675",n:"19",lat:"-64.4754",lon:"84.8627",x:"1320px",y:"770px",x7:"1300px",y7:"765px",s:"9px"},{id:"311351",n:"23",lat:"-75.3988",lon:"75.0211",x:"1275px",y:"825px",x7:"1280px",y7:"810px",s:"11px"},{id:"378848",n:"17",lat:"-83.3697",lon:"26.1640",x:"1030px",y:"865px",x7:"1020px",y7:"865px",s:"8px"},{id:"819096",n:"42",lat:"-84.6263",lon:"-22.7659",x:"785px",y:"870px",x7:"885px",y7:"880px",s:"21px"},{id:"015235",n:"25",lat:"-73.3436",lon:"-54.1617",x:"625px",y:"815px",x7:"585px",y7:"820px",s:"12px"},{id:"472821",n:"15",lat:"-78.5673",lon:"-45.9861",x:"670px",y:"840px",x7:"1115px",y7:"850px",s:"7px"},{id:"065852",n:"20",lat:"-76.6232",lon:"-75.3590",x:"520px",y:"830px",x7:"555px",y7:"835px",s:"10px"},{id:"412964",n:"25",lat:"-83.0222",lon:"-77.4331",x:"510px",y:"865px",x7:"1795px",y7:"865px",s:"12px"},{id:"241663",n:"70",lat:"-64.9849",lon:"-72.0578",x:"535px",y:"770px",x7:"610px",y7:"775px",s:"35px"},{id:"005324",n:"22",lat:"-51.5140",lon:"-63.9106",x:"580px",y:"705px",x7:"455px",y7:"710px",s:"11px"},{id:"710337",n:"25",lat:"-36.3014",lon:"-57.4005",x:"610px",y:"630px",x7:"595px",y7:"630px",s:"12px"},{id:"405378",n:"22",lat:"-18.3761",lon:"-126.4726",x:"265px",y:"540px",x7:"270px",y7:"520px",s:"11px"},{id:"455388",n:"20",lat:"-29.0470",lon:"-129.1007",x:"250px",y:"595px",x7:"250px",y7:"600px",s:"10px"},{id:"264056",n:"20",lat:"-47.2972",lon:"-127.8187",x:"260px",y:"685px",x7:"260px",y7:"690px",s:"10px"},{id:"271807",n:"26",lat:"-57.4031",lon:"-117.9551",x:"310px",y:"735px",x7:"330px",y7:"750px",s:"13px"},{id:"069415",n:"44",lat:"-67.5988",lon:"-108.1395",x:"300px",y:"785px",x7:"300px",y7:"795px",s:"22px"},{id:"975300",n:"21",lat:"-80.4381",lon:"-112.0883",x:"335px",y:"850px",x7:"1795px",y7:"860px",s:"10px"},{id:"799966",n:"69",lat:"-90.4621",lon:"-106.5648",x:"335px",y:"900px",x7:"315px",y7:"880px",s:"34px"},{id:"135527",n:"16",lat:"-67.9793",lon:"-132.5344",x:"235px",y:"785px",x7:"220px",y7:"790px",s:"8px"},{id:"152437",n:"19",lat:"-29.5633",lon:"-133.6323",x:"230px",y:"595px",x7:"230px",y7:"600px",s:"9px"},{id:"257628",n:"67",lat:"-12.4644",lon:"-139.7750",x:"200px",y:"510px",x7:"180px",y7:"500px",s:"33px"},{id:"503164",n:"19",lat:"-1.4248",lon:"-162.0521",x:"85px",y:"455px",x7:"95px",y7:"445px",s:"9px"},{id:"138083",n:"21",lat:"23.6997",lon:"-167.2080",x:"60px",y:"330px",x7:"25px",y7:"330px",s:"10px"},{id:"273103",n:"70",lat:"43.8809",lon:"-167.9020",x:"60px",y:"230px",x7:"70px",y7:"240px",s:"35px"},{id:"283031",n:"64",lat:"50.6042",lon:"-161.0307",x:"90px",y:"195px",x7:"10px",y7:"195px",s:"32px"},{id:"333831",n:"21",lat:"37.9917",lon:"-176.4254",x:"15px",y:"260px",x7:"20px",y7:"265px",s:"10px"},{id:"614181",n:"30",lat:"25.9310",lon:"-174.1178",x:"25px",y:"320px",x7:"75px",y7:"320px",s:"15px"},{id:"502574",n:"51",lat:"79.5169",lon:"-137.3941",x:"210px",y:"50px",x7:"210px",y7:"40px",s:"25px"},{id:"300997",n:"67",lat:"80.9574",lon:"-129.0782",x:"250px",y:"45px",x7:"255px",y7:"35px",s:"33px"},{id:"810080",n:"16",lat:"83.3407",lon:"-117.9974",x:"310px",y:"30px",x7:"295px",y7:"25px",s:"8px"},{id:"895790",n:"94",lat:"-37.2974",lon:"-171.1844",x:"40px",y:"635px",x7:"50px",y7:"630px",s:"47px"},{id:"001182",n:"22",lat:"-62.5514",lon:"-163.1027",x:"80px",y:"760px",x7:"1795px",y7:"760px",s:"11px"},{id:"430441",n:"89",lat:"-65.2534",lon:"-149.3925",x:"150px",y:"775px",x7:"1785px",y7:"780px",s:"44px"},{id:"390247",n:"20",lat:"20.2944",lon:"-171.6732",x:"40px",y:"345px",x7:"15px",y7:"345px",s:"10px"},{id:"429339",n:"20",lat:"8.4117",lon:"-174.1584",x:"25px",y:"405px",x7:"40px",y7:"385px",s:"10px"},{id:"834455",n:"27",lat:"-12.7855",lon:"-168.8450",x:"55px",y:"510px",x7:"35px",y7:"505px",s:"13px"},{id:"516420",n:"24",lat:"-17.6772",lon:"-153.3953",x:"130px",y:"535px",x7:"45px",y7:"520px",s:"12px"},{id:"357643",n:"70",lat:"-29.6333",lon:"-145.2832",x:"170px",y:"595px",x7:"165px",y7:"600px",s:"35px"},{id:"707617",n:"66",lat:"-32.4667",lon:"-158.1028",x:"105px",y:"610px",x7:"170px",y7:"605px",s:"33px"},{id:"354815",n:"25",lat:"-10.0689",lon:"-165.0124",x:"70px",y:"500px",x7:"80px",y7:"490px",s:"12px"},{id:"856750",n:"20",lat:"-8.4729",lon:"-173.2200",x:"30px",y:"490px",x7:"1795px",y7:"475px",s:"10px"},{id:"572730",n:"24",lat:"-17.8328",lon:"-137.0496",x:"210px",y:"535px",x7:"215px",y7:"530px",s:"12px"},{id:"472573",n:"73",lat:"2.1570",lon:"182.3879",x:"1810px",y:"435px",x7:"0px",y7:"420px",s:"36px"},{id:"063596",n:"17",lat:"-6.1465",lon:"153.9488",x:"1665px",y:"480px",x7:"1615px",y7:"455px",s:"8px"},{id:"333209",n:"19",lat:"-7.8441",lon:"142.8063",x:"1610px",y:"485px",x7:"1755px",y7:"460px",s:"9px"},{id:"988959",n:"19",lat:"11.2960",lon:"134.2167",x:"1570px",y:"390px",x7:"1560px",y7:"390px",s:"9px"},{id:"043058",n:"15",lat:"12.8908",lon:"143.6974",x:"1615px",y:"385px",x7:"1610px",y7:"390px",s:"7px"},{id:"855507",n:"87",lat:"-10.5319",lon:"150.6688",x:"1650px",y:"500px",x7:"1795px",y7:"480px",s:"43px"},{id:"244402",n:"19",lat:"-63.6610",lon:"159.7054",x:"1695px",y:"765px",x7:"1680px",y7:"800px",s:"9px"},{id:"670307",n:"32",lat:"-75.1781",lon:"155.3944",x:"1675px",y:"825px",x7:"1650px",y7:"855px",s:"16px"},{id:"404140",n:"86",lat:"-62.3409",lon:"191.7847",x:"1855px",y:"760px",x7:"1795px",y7:"770px",s:"43px"},{id:"704317",n:"21",lat:"-85.7172",lon:"185.7677",x:"1825px",y:"875px",x7:"1785px",y7:"890px",s:"10px"},{id:"344033",n:"26",lat:"-82.1861",lon:"110.6955",x:"1450px",y:"860px",x7:"1460px",y7:"865px",s:"13px"},{id:"149518",n:"24",lat:"3.0029",lon:"168.8779",x:"1740px",y:"430px",x7:"1750px",y7:"410px",s:"12px"},{id:"174628",n:"35",lat:"16.4167",lon:"156.2071",x:"1650px",y:"365px",x7:"1665px",y7:"380px",s:"17px"},{id:"274106",n:"27",lat:"34.2786",lon:"148.1460",x:"1640px",y:"275px",x7:"1585px",y7:"280px",s:"13px"},{id:"863002",n:"21",lat:"43.9992",lon:"146.9222",x:"1630px",y:"230px",x7:"1755px",y7:"235px",s:"10px"},{id:"805604",n:"17",lat:"-58.5690",lon:"-35.7378",x:"720px",y:"740px",x7:"660px",y7:"750px",s:"8px"},{id:"091041",n:"32",lat:"-43.1748",lon:"-34.9354",x:"725px",y:"665px",x7:"635px",y7:"675px",s:"16px"}],
			mousePosX:"",
			mousePosY:"",
			prevMousePosX:"",
			prevMousePosY:"",
			mouseDownReal:"false",
			left:"0",
			top:"0",
			xcoords:[],
			ycoords:[],
			minSize:15,
		}
	},
	watch:{
		minSize(newMinSize){
			
			var elements=document.getElementsByClassName("info");
			for(var i=0;i<elements.length;i++){
				
					elements[i].classList.add("invis");
				
			}
			var elements=document.getElementsByClassName("outer");
			for(var i=0;i<elements.length;i++){
				
					elements[i].style.backgroundColor="rgb(240, 67, 67)";
				
			}
			document.getElementById("infofake").style.display="none";
			
			var trails=document.getElementsByClassName("trail");
			for(var i=0;i<elements.length;i++){
				
					trails[i].classList.add("invis");
				
			}
			document.getElementById("infofake").style.display="block";
		}
	},
	computed:{
		css(){
			return{
				"--left":this.left+"px",
				"--top":this.top+"px",
			}
		},
		activeDots(){
			var min=this.minSize;
			return this.trashes.filter(function(u){
				return parseInt(u.n)>=min;
			})
		}
	},
	methods:{
		mouseDown:function(){
			this.mouseDownReal="true";
			this.xcoords.push(this.mousePosX);
			this.ycoords.push(this.mousePosY);
			var output="[";
			for(var i=0;i<this.xcoords.length;i++){
				output+="("+this.xcoords[i]+", "+this.ycoords[i]+"),";
			}
			//console.log(output);
			//console.log(this.mousePosX+" "+this.mousePosY);
		},
		mouseUp:function(){
			this.mouseDownReal="false";
		},
		countDown(){
			var dx=(this.mousePosX-this.prevMousePosX);
			var dy=(this.mousePosY-this.prevMousePosY);
			
			if(this.mouseDownReal=="true"){
			
			
				this.left=parseInt(this.left)+dx*1;
				localStorage.setItem("left",this.left);
				this.top=parseInt(this.top)+dy*1;
				localStorage.setItem("top",this.top);
			}
		}
	},
	mounted(){
		document.getElementById('my-image').ondragstart = function() { return false; };
		localStorage.setItem("left","0");
		localStorage.setItem("top","0");
		document.addEventListener("mousemove", (event) => {
			this.prevMousePosX=this.mousePosX;
			this.prevMousePosY=this.mousePosY;
			this.mousePosX = event.clientX;
			this.mousePosY = event.clientY;
		});
		this.$nextTick(function () {
            window.setInterval(() => {
                this.countDown();
				this.prevMousePosX=this.mousePosX;
				this.prevMousePosY=this.mousePosY;
            },10);
        })
	
	}
}
	
</script>
<style scoped>
body{
	
}


#slide{
	position:absolute;
	left:50%;
	top:80%;
	border-radius:5px;
	width:100%;
	height:50px;
	overflow:hidden;
	border:2.5px solid rgb(0,0,0,0.3);
	-webkit-appearance:none;
	border-radius:10px;
	font-size:80px;
	padding-left:10px;
	padding-right:10px;
	transition:0.1s all;
}
#slide:focus{
	border:2.5px solid rgb(61, 131, 245);
	outline:none;
}
#slide::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  border-radius:20px;
  background: rgb(61, 131, 245);
  cursor: pointer;
}
.slidecontainer {
  width: 15%; 
  position:absolute;
  left:75%;
  height:100px;
  top:84%;
  border-radius:20px;
  
 
  
}
#slidelabel{
	position:absolute;
	font-size:25px;
	color:rgba(0,0,0,0.7);
	left:100%;
	width:200px;
	top:45%;
}
#slidemin{
	position:absolute;
	font-size:20px;
	color:rgba(0,0,0,0.7);
	left:55%;
	width:20px;
	top:95%;
}
#slidemax{
	position:absolute;
	font-size:20px;
	color:rgba(0,0,0,0.7);
	left:142%;
	width:20px;
	top:95%;
}

#infofake{
	background-color:rgb(245,245,245);
	
	position:absolute;
	left:1690px;
	width:200px;
	top:3%;
	height:33%;
	border-radius:50px 50px 50px 50px;
	border:2.5px solid rgba(0,0,0,0.3);
	z-index:1000;
}
#back{
	background:transparent;
	width:100%;
	height:100%;
	position:absolute;
	left:0%;
	top:0%;
	
}
.invis{
	opacity:0;
}
#id{
	position:absolute;
	width:70%;
	left:15%;
	top:60%;
	height:10%;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:white;
	font-size:20px;
	color:rgba(0,0,0,0.7);
	
}
#num{
	font-size:60px;
	position:absolute;
	width:100px;
	left:25%;
	top:25%;
	height:100px;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:rgb(240, 67, 67);
	border-radius:50px;
	border:3px dashed rgb(240, 67, 67);
}
#numfake{
	font-size:70px;
	position:absolute;
	width:150px;
	left:12%;
	top:20%;
	height:100px;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:rgb(240, 67, 67);
	border-radius:50px;
	
}
#numlabel{
	position:absolute;
	width:100%;
	left:0%;
	top:65%;
	height:10%;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:white;
	font-size:20px;
}
#location{
	position:absolute;
	width:100%;
	left:0%;
	top:80%;
	height:10%;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:white;
	font-size:17px;
}




#Background{
	overflow:hidden;
	background-color:rgb(245,245,245);
	position:absolute;
	left:0%;
	top:0%;
	width:100%;
	height:100%;
}
img{
	width:1920px;
	height:980px;
	position:absolute;
	filter:brightness(120%);
	left:var(--left);
	top:var(--top);
	
}

</style>