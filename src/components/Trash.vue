<template>
	<div id="outer" :style="css"></div>
	
</template>
<script>
export default{
	props:["x","y"],
	computed:{
		css(){
			return{
				"--x":this.x,
				"--y":this.y,
			}
		}
	},
}
</script>
<style scoped>
#outer{
	background-color:rgb(240, 67, 67);
	width:20px;
	height:20px;
	border-radius:20px;
	position:absolute;
	left:var(--x);
	top:var(--y);
	
}
#inner{
	background-color:rgb(219, 0, 0);
	width:15px;
	height:15px;
	border-radius:20px;
	position:absolute;
	left:calc(var(--x) + 2.5px);
	top:calc(var(--y) + 2.5px);
}
</style>