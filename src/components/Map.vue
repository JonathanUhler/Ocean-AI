<template>
	<div id="Background">
		<img :src="require(`../assets/world3.svg`)" />
		<div id="infofake">
		<!--<div id="id"><b>TOTAL</b></div>
		<div id="numfake"><b>100K</b></div>
		<div id="numlabel">pieces of trash</div>
		<div id="location">📍 300+ Trash Heaps 📍</div>
		</div>
		-->
	</div>
		<Trash x="500px" y="200px" x7="520px" y7="350px" s="20px" n="14" lat="22.3545" log="33.5634" nu="0" id="252583"></Trash>
		<Trash x="500px" y="500px" x7="550px" y7="540px" s="30px" n="37" lat="22.3545" log="33.5634" nu="1" id="123456"></Trash>
	</div>
	
</template>
<script>
import Trash from "./Trash.vue";
export default{
	components:{
		Trash
	},
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
	width:100%;
	left:0%;
	top:8%;
	height:10%;
	display:flex;
	justify-content:center;
	align-items:center;
	text-align:center;
	color:white;
	font-size:25px;
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
	background-color:rgb(235,235,235);
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
	left:30px;
}
</style>