import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Home.vue'
import Project from '../views/Controller.vue'
import Teams from '../views/Settings.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Dashboard
  },
  {
    path: '/Controller',
    name: 'Controller',
    component: Project
  },
  {
    path: '/Settings',
    name: 'Settings',
    component: Teams

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
