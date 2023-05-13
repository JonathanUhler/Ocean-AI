<template>
	<!--<div id="back" v-on:click="hide"></div>-->
	<div v-on:click="reveal" id="outer" :style="css"></div>
	
	<div class="info invis" >
		<div id="id"><b>ID #{{id}}</b></div>
		<div id="num"><b>{{n}}</b></div>
		<div id="numlabel">pieces of trash</div>
		<div id="location">📍 {{lat}} {{log}} 📍</div>
		<button id="current"><b>Current</b></button>
		<button id="week"><b>7 Days</b></button>
	</div>
</template>
<script>
export default{
	props:["x","y","s","n","lat","log","nu","id"],
	computed:{
		css(){
			return{
				"--x":this.x,
				"--y":this.y,
				"--s":this.s,
			}
		}
	},
	methods:{
		reveal:function(){
			var elements=document.getElementsByClassName("info");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					elements[i].classList.remove("invis");
				}else{
					elements[i].classList.add("invis");
				}
			}
			//document.getElementsByClassName("info")[parseInt(this.num)].classList.remove("invis");
		},
		hide:function(){
			document.getElementsByClassName("info")[parseInt(this.num)].classList.add("invis");
		}
	}
}
</script>
<style scoped>
#outer{
	background-color:rgb(240, 67, 67);
	width:var(--s);
	height:var(--s);
	border-radius:1000px;
	position:absolute;
	left:var(--x);
	top:var(--y);
	border:calc(var(--s) / 10) solid rgb(50,50,50);
	transition:0.2s all;
}
#outer:hover{
	transform:scale(1.1);
}
.info{
	background-color:rgb(30,30,30);
	position:absolute;
	left:1690px;
	width:200px;
	top:3%;
	height:30%;
	border-radius:50px 50px 0px 0px;
	
	transition:0.1s all;
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
#current{
	background-color:rgb(61, 131, 245);
	color:white;
	border:none;
	outline:none;
	position:absolute;
	left:0%;
	top:100%;
	width:50%;
	height:10%;
	font-family: 'Open Sans', sans-serif;
	border-radius:0px 0px 0px 20px;
	display:flex;
	justify-content:center;
	align-items:center;
}
#week{
	background-color:transparent;
	color:white;
	border:none;
	outline:none;
	position:absolute;
	left:50%;
	top:100%;
	width:50%;
	height:10%;
	font-family: 'Open Sans', sans-serif;
	color:rgb(61,131,245);
	border-radius:0px 0px 20px 0px;
	border:2px solid rgb(61,131,245);
	display:flex;
	justify-content:center;
	align-items:center;
}

</style>