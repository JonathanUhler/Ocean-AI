<template>
	<div v-if="this.sid=='left'" :style="css" id="Feature">
		<div id="Pitch"><b>{{mp}}</b></div>
		<div id="SubPitch">{{sp}}</div>
		<img :src="require(`../assets/${i}`)" />
		<VButton x="29%" y="79%" c="blue" t="Learn More" s="smallmedium" L="/"></VButton>
	</div>
	<div v-else :style="css" id="Feature">
		<div id="PitchR"><b>{{mp}}</b></div>
		<div id="SubPitchR">{{sp}}</div>
		<img id="imgR" :src="require(`../assets/${i}`)" />
		<VButton x="59%" y="79%" c="blue" t="Learn More" s="smallmedium" L="/"></VButton>
	</div>
</template>
<script>
import VButton from "./VButton.vue";
export default{
	
	props:["y","c","mp","sp","i","side","iw","ih","iy","ix"],
	data(){
		return{
			sid:""
		}
	},
	computed:{
		css(){
			return{
				"--y":this.y,
				"--c":this.c,
				"--iw":this.iw,
				"--ih":this.ih,
				"--iy":this.iy,
				"--ix":this.ix,
			}
		}
	},
	mounted(){
		if(this.side=="left"){
			this.sid="left";
		}else{
			this.sid="right";
		}
	},
	components:{
	VButton,
	}
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
#Feature{
	position:absolute;
	left:0%;
	top:var(--y);
	width:100%;
	height:500px;
	background-color:var(--c);
	font-family: 'Open Sans', sans-serif;
}
#Pitch{
	position:absolute;
	width:30%;
	height:20%;
	left:18%;
	top:25%;
	display:flex;
	align-items:center;
	font-size:40px;
	font-family: 'Open Sans', sans-serif;
	text-align:left;
	color:rgb(60,60,60);

}
#SubPitch{
	position:absolute;
	width:30%;
	height:50%;
	left:20%;
	top:35%;
	display:flex;
	justify-content:center;
	align-items:center;
	font-size:22px;
	font-family: 'Open Sans', sans-serif;
	text-align:left;
}
img{
	width:var(--iw);
	height:var(--ih);
	position:absolute;
	left:55%;
	top:var(--iy);
	border-radius:10px;
	filter:saturate(120%);
	
}

#PitchR{
	position:absolute;
	width:30%;
	height:20%;
	left:50%;
	top:25%;
	display:flex;
	align-items:center;
	font-size:40px;
	font-family: 'Open Sans', sans-serif;
	text-align:left;
	color:rgb(60,60,60);
	
}
#SubPitchR{
	position:absolute;
	width:30%;
	height:50%;
	left:50%;
	top:35%;
	display:flex;
	justify-content:center;
	align-items:center;
	font-size:22px;
	font-family: 'Open Sans', sans-serif;
	text-align:left;
}
#imgR{
	width:var(--iw);
	height:var(--ih);
	position:absolute;
	left:var(--ix);
	top:var(--iy);
	border-radius:10px;
	filter:saturate(120%);
	
}

</style>