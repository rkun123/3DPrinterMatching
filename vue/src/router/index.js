import Vue from 'vue'
import VueRouter from 'vue-router'
import Start from '../views/Start.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import Main from '../views/UserMainpage.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Start',
    component: Start
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
