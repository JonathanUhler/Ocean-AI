<template>
	<!--<div class="trail invis" :style="css"></div>-->
	<div v-on:click="reveal" class="outer" :style="css"></div>
	
	<div class="info invis" >
		<div id="id"><b>ID #{{id}}</b></div>
		<div id="num"><b>{{n}}</b></div>
		<div id="numlabel">pieces of trash</div>
		<div id="location">📍 {{lat}} {{log}} 📍</div>
		<button  v-on:click="predictcurrent" class="current currentselect"><b>Current</b></button>
		<button v-on:click="predict7" class="week"><b>7 Days</b></button>
	</div>
</template>
<script>
export default{
	props:["x","y","x7","y7","s","n","lat","log","nu","id"],
	data(){
		return{
			angle:"",
			distance:"",
			left:"0",
			top:"0",
		}
	},
	computed:{
		css(){
			return{
				"--x":(parseInt(this.x)-160)+"px",
				"--y":(parseInt(this.y)-30)+"px",
				"--s":this.s,
				"--x7":(parseInt(this.x7)-160)+"px",
				"--y7":(parseInt(this.y7)-30)+"px",
				"--ta":this.angle,
				"--tw":this.distance,
				"--left":(parseInt(this.left)+180)+"px",
				"--top":this.top+"px",
			}
		}
	},
	mounted(){
		var angleDeg=(180/Math.PI)*Math.atan((parseInt(this.y)-parseInt(this.y7))/(parseInt(this.x)-parseInt(this.x7)));
		var distance=Math.sqrt(((parseInt(this.y)-parseInt(this.y7))*((parseInt(this.y)-parseInt(this.y7))))+((parseInt(this.x)-parseInt(this.x7))*((parseInt(this.x)-parseInt(this.x7)))));
		this.angle=angleDeg+"deg";
		this.distance=distance+"px";
		//console.log(angleDeg+" "+this.distance);
		this.$nextTick(function () {
            window.setInterval(() => {
                this.countDown();
				
            },10);
        })
		
	},
	methods:{
		reveal:function(){
			console.log(this.nu);
			var elements=document.getElementsByClassName("info");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					elements[i].classList.remove("invis");
				}else{
					elements[i].classList.add("invis");
				}
			}
			var elements=document.getElementsByClassName("outer");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					elements[i].style.backgroundColor="rgb(61,131,245)";
				}else{
					elements[i].style.backgroundColor="rgb(240, 67, 67)";
				}
			}
			document.getElementById("infofake").style.display="none";
			this.predictcurrent();
			
		},
		predict7:function(){
			var elements=document.getElementsByClassName("outer");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					elements[i].classList.add("predict7");
					
				}else{
					elements[i].classList.remove("predict7");
				}
			}
			var buttons=document.getElementsByClassName("week");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					buttons[i].classList.add("weekselect");
					
				}else{
					buttons[i].classList.remove("weekselect");
				}
			}
			var buttons2=document.getElementsByClassName("current");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					buttons2[i].classList.remove("currentselect");
					
				}else{
					buttons2[i].classList.add("currentselect");
				}
			}
			/*
			var trails=document.getElementsByClassName("trail");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					trails[i].classList.remove("invis");
					
				}else{
					trails[i].classList.add("invis");
				}
			}
			*/
			
		},
		predictcurrent:function(){
			var elements=document.getElementsByClassName("outer");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					elements[i].classList.remove("predict7");
					
				}else{
					elements[i].classList.remove("predict7");
				}
			}
			var buttons=document.getElementsByClassName("week");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					buttons[i].classList.remove("weekselect");
					
				}else{
					buttons[i].classList.remove("weekselect");
				}
			}
			var buttons2=document.getElementsByClassName("current");
			for(var i=0;i<elements.length;i++){
				if(i==parseInt(this.nu)){
					buttons2[i].classList.add("currentselect");
					
				}else{
					buttons2[i].classList.add("currentselect");
				}
			}
		},
		countDown(){
				this.left=localStorage.getItem("left");
				if(this.left==null)this.left="0";
				this.top=localStorage.getItem("top");
				if(this.top==null)this.top="0";
				if(localStorage.getItem("Search ID:")==this.id){
					this.reveal();
					localStorage.setItem("Search ID:","0");
				}
		}
	}
}
</script>
<style scoped>
.outer{
	background-color:rgb(240, 67, 67);
	width:var(--s);
	height:var(--s);
	border-radius:1000px;
	position:absolute;
	left:calc(var(--x) + var(--s) / 2 + var(--left));
	top:calc(var(--y) + var(--s) / 2 + var(--top));
	border:calc(var(--s) / 10) solid rgb(50,50,50);
	transition:0.2s transform;
}
.outer:hover{
	transform:scale(1.1);
}
.predict7{
	animation-name:move7;
	animation-duration:2s;
	animation-fill-mode:forwards;
	animation-timing-function:ease-out;
}
@keyframes move7{
	0%{left:calc((var(--x)) + ((var(--s) / 2)) + (var(--left)));top:calc((var(--y)) + (var(--s) / 2) + (var(--top)));}
	100%{left:calc((var(--x7)) + (var(--s) / 2) + (var(--left)));top:calc((var(--y7)) + (var(--s) / 2) + (var(--top)));}
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
	z-index:999;
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
.trail{
	width:calc(var(--tw) + 10px);
	transform:rotate(var(--ta));
	position:absolute;
	left:calc(var(--x) + 5px);
	top:calc(var(--y) + 25px);
	background-color:rgb(240, 67, 67);
	height:10px;
	border-radius:10px;
	animation-name:expand;
	animation-duration:3s;
}

.invis{
	display:none;
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
.current{
	background-color:rgb(245,245,245);
	
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
	color:rgb(61,131,245);
	border:2px solid rgb(61,131,245);
}
.currentselect{
	background-color:rgb(61, 131, 245);
		color:white;
	}
.week{
	background-color:rgb(245,245,245);
	
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
	transition:0.1s all;
}
.weekselect{
	background-color:rgb(61, 131, 245);
	color:white;
}

</style>