<template>
  <a v-if="scroll==''" :href="L" :style="css"><b>{{t}}</b></a>
  <router-link v-else :to="L" :style="css"><b>{{t}}</b></router-link>
  
</template>

<script>
export default{
	props:["x","y","o","t","c","L","s","scroll"],
	
	computed:{
		css(){
			return{
				"--x":this.x,
				"--y":this.y,
				"--tc":this.tc,
				"--bc":this.bc,
				"--oc":this.oc,
				"--w":this.w,
				"--h":this.h,
				"--fs":this.fs,
				"--bs":this.bs,
			}
		}
	},
	data(){
		return{
			bc:"",
			tc:"",
			oc:"",
			size:"",
			fs:"",
			bs:"",
		}
	},
	mounted(){
		if(this.o==""){
			this.bc="white";
			if(this.c=="blue"){
				this.tc="rgb(61, 131, 245)";
				this.oc="rgb(61, 131, 245)";
			}else if(this.c=="red"){
				this.tc="rgb(245, 61, 61)";
				this.oc="rgb(245, 61, 61)";
			}else if(this.c=="orange"){
				this.tc="rgb(230, 185, 73)";
				this.oc="rgb(230, 185, 73)";
			}else if(this.c=="green"){
				this.tc="rgb(73, 230, 94)";
				this.oc="rgb(73, 230, 94)";
			}else if(this.c=="purple"){
				this.tc="rgb(154, 73, 230)";
				this.oc="rgb(154, 73, 230)";
			}
		}else{
			this.tc="white";
			this.oc="white";
			if(this.c=="blue"){
				this.bc="rgb(61, 131, 245)";
			}else if(this.c=="red"){
				this.bc="rgb(245, 61, 61)";
			}else if(this.c=="orange"){
				this.bc="rgb(230, 185, 73)";
			}else if(this.c=="green"){
				this.bc="rgb(73, 230, 94)";
			}else if(this.c=="purple"){
				this.bc="rgb(154, 73, 230)";
			}
		}
		if(this.s=="small"){
			this.w="120px";
			this.h="50px";
			this.fs="20px";
			this.bs="2px";
		}
		if(this.s=="smallmedium"){
			this.w="180px";
			this.h="60px";
			this.fs="25px";
			this.bs="2px";
		}
		if(this.s=="medium"){
			this.w="220px";
			this.h="70px";
			this.fs="30px";
			this.bs="2.5px";
		}
		if(this.s=="large"){
			this.w="400px";
			this.h="140px";
			this.fs="60px";
			this.bs="4px"
		}
	}
	
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');
a{
	width:var(--w);
	height:var(--h);
	position:absolute;
	left:var(--x);
	top:var(--y);
	background-color:var(--bc);
	border:var(--bs) solid var(--oc);
	color:var(--tc);
	font-size:var(--fs);
	border-radius:10px;
	text-align:center;
	display: inline-flex;
    justify-content: center; /* center the content horizontally */
    align-items: center;
	text-decoration:none;
	font-family: 'Open Sans', sans-serif;
	transition:0.2s all;
}
a:hover{
	transform:scale(0.95);
	filter:brightness(106%);
}
</style>
