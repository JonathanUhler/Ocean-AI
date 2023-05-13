import {createApp} from 'vue'
import {createRouter,createWebHistory} from 'vue-router'
import App from './App.vue'

import Home from "./components/Home"
import Map from "./components/Map"

const router=createRouter({
	history:createWebHistory(),
	routes:[
	{path:"/",component:Home},
	{path:"/map",component:Map}
	]
})

const app=createApp(App)
app.use(router)
app.mount('#app')
