<template>
	<div :style="css">{{t}}</div>
	<input v-if="p==''" :style="css" type="password" v-model="in">
	<input v-else :style="css" v-model="in">
</template>
<script>
export default{
	props:["x","y","c","t","s","p"],
	data(){
		return{
			in:"",
			color:"",
			w:"",
			h:"",
		}
	},
	watch:{
		in(newIn){
			localStorage.setItem(this.t,newIn);
		}
	},
	computed:{
		css(){
			return{
				"--x":this.x,
				"--y":this.y,
				"--c":this.color,
				"--w":this.w,
				"--h":this.h,
			}
		}
	},
	mounted(){
		if(this.c=="blue"){
			this.color="rgb(61, 131, 245)";
		}
		if(this.s=="medium"){
			this.w="300px";
			this.h="40px";
		}
		
	}
}
</script>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');

<style scoped>
input{
	position:absolute;
	left:var(--x);
	top:var(--y);
	width:var(--w);
	height:var(--h);
	border:2.5px solid rgba(0,0,0,0.3);
	border-radius:10px;
	transition:0.1s all;
	padding-left:5px;
	font-family: 'Open Sans', sans-serif;
	font-size:20px;
}
input:focus{
	border:2.5px solid var(--c);
	outline:none;
}

div{
	font-family: 'Open Sans', sans-serif;
	position:absolute;
	left:var(--x);
	top:calc(var(--y) - 40px);
	font-size:25px;
	color:rgba(0,0,0,0.7);
}

</style>