<template>
	
	<div id="Background">
		<img :src="require(`../assets/world3.svg`)" />
		<div id="infofake">
		<div id="numfake">✅</div>
		<div id="id"><b>Click a Red Dot to Begin</b></div>
		</div>
		
		<!--<div id="numfake"><b>100K</b></div>
		<div id="numlabel">pieces of trash</div>
		<div id="location">📍 300+ Trash Heaps 📍</div>
		</div>
		-->
	</div>
	<VButton x="1.5%" y="2%" t="Back" c="blue" s="small" L="/"></VButton>
	<div v-for="(trash,index) in trashes">
		<Trash :x="trash.x" :y="trash.y" :x7="trash.x7" :y7="trash.y7" :s="trash.s" :n="trash.n" :lat="trash.lat" :log="trash.lon" :id="trash.id" :nu="index"></Trash>
	</div>
	
	
</template>
<script>
import Trash from "./Trash.vue";
import VButton from "./VButton.vue";
export default{
	components:{
		Trash,
		VButton
	},
	data(){
		return{
			trashes:[{id:"168246",n:"58",lat:"32.4910",lon:"-136.8220",x:"230px",y:"313px",x7:"320px",y7:"297px",s:"58px"},{id:"73af16",n:"5",lat:"31.8300",lon:"-133.9190",x:"245px",y:"316px",x7:"264px",y7:"324px",s:"5px"},{id:"167926",n:"5",lat:"30.3630",lon:"-132.2160",x:"254px",y:"324px",x7:"225px",y7:"328px",s:"5px"},{id:"a78a0e",n:"5",lat:"28.0310",lon:"-131.4310",x:"259px",y:"337px",x7:"290px",y7:"311px",s:"5px"},{id:"160825",n:"1",lat:"21.2900",lon:"-157.8250",x:"118px",y:"374px",x7:"200px",y7:"442px",s:"1px"},{id:"33318c",n:"5",lat:"34.9870",lon:"-152.9660",x:"144px",y:"299px",x7:"231px",y7:"365px",s:"5px"},{id:"fb30c8",n:"38",lat:"36.8160",lon:"-142.1600",x:"201px",y:"289px",x7:"292px",y7:"311px",s:"38px"},{id:"35226e",n:"22",lat:"32.4740",lon:"-145.4580",x:"184px",y:"313px",x7:"191px",y7:"389px",s:"22px"},{id:"168108",n:"53",lat:"33.3750",lon:"-135.6850",x:"236px",y:"308px",x7:"333px",y7:"286px",s:"53px"},{id:"9374c2",n:"9",lat:"38.5650",lon:"-134.1800",x:"244px",y:"280px",x7:"655px",y7:"337px",s:"9px"},{id:"165841",n:"12",lat:"32.3540",lon:"-120.7080",x:"316px",y:"313px",x7:"307px",y7:"303px",s:"12px"},{id:"b44829",n:"6",lat:"29.5830",lon:"-134.4620",x:"242px",y:"328px",x7:"3px",y7:"265px",s:"6px"},{id:"e2d6ff",n:"10",lat:"36.8260",lon:"-140.0940",x:"212px",y:"289px",x7:"188px",y7:"349px",s:"10px"},{id:"4c85a6",n:"7",lat:"30.1410",lon:"-144.0040",x:"191px",y:"325px",x7:"12px",y7:"261px",s:"7px"},{id:"cadd11",n:"28",lat:"30.8400",lon:"-141.7470",x:"204px",y:"322px",x7:"87px",y7:"390px",s:"28px"},{id:"d66677",n:"11",lat:"33.0890",lon:"-153.0460",x:"143px",y:"309px",x7:"1917px",y7:"328px",s:"11px"},{id:"107435",n:"6",lat:"37.2860",lon:"-149.5970",x:"162px",y:"286px",x7:"156px",y7:"361px",s:"6px"},{id:"52feb0",n:"4",lat:"27.2570",lon:"-152.8320",x:"144px",y:"341px",x7:"391px",y7:"279px",s:"4px"},{id:"167959",n:"32",lat:"36.8530",lon:"-35.1010",x:"772px",y:"289px",x7:"714px",y7:"337px",s:"32px"},{id:"6dee9a",n:"1",lat:"39.4280",lon:"-33.6410",x:"780px",y:"275px",x7:"669px",y7:"370px",s:"1px"},{id:"803206",n:"6",lat:"2.9840",lon:"-17.0640",x:"868px",y:"473px",x7:"775px",y7:"425px",s:"6px"},{id:"6f4ea3",n:"13",lat:"-15.7180",lon:"-6.0030",x:"927px",y:"575px",x7:"904px",y7:"518px",s:"13px"},{id:"167281",n:"3",lat:"-34.0220",lon:"18.4200",x:"1058px",y:"675px",x7:"1208px",y7:"685px",s:"3px"},{id:"161908",n:"92",lat:"-6.7150",lon:"39.2230",x:"1169px",y:"526px",x7:"1111px",y7:"465px",s:"92px"},{id:"168113",n:"89",lat:"50.0990",lon:"-1.2560",x:"953px",y:"217px",x7:"1183px",y7:"143px",s:"89px"},{id:"164026",n:"9",lat:"8.6710",lon:"77.0860",x:"1371px",y:"442px",x7:"1373px",y7:"424px",s:"9px"},{id:"163249",n:"51",lat:"3.1870",lon:"101.6080",x:"1501px",y:"472px",x7:"1498px",y7:"451px",s:"51px"},{id:"162390",n:"54",lat:"-7.3430",lon:"112.6950",x:"1561px",y:"529px",x7:"1911px",y7:"409px",s:"54px"},{id:"168181",n:"13",lat:"33.5790",lon:"130.2670",x:"1654px",y:"307px",x7:"1648px",y7:"333px",s:"13px"},{id:"166215",n:"21",lat:"34.0300",lon:"141.0500",x:"1712px",y:"304px",x7:"1755px",y7:"356px",s:"21px"}],
		}
	}
}
	
</script>
<style scoped>
body{
	
}




#infofake{
	background-color:rgb(30,30,30);
	position:absolute;
	left:1690px;
	width:200px;
	top:3%;
	height:30%;
	border-radius:50px 50px 0px 0px;
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
	font-size:50px;
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
	left:250px;
	top:0px;
}
</style>