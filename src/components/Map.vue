<template>
	<div id="Background">
		<img :src="require(`../assets/worldmap2.png`)" />
		<Trash x="40%" y="20%"></Trash>
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
#Background{
	overflow:hidden;
	background-color:rgb(50,50,50);
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
}
</style>