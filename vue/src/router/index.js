import Vue from 'vue'
import VueRouter from 'vue-router'
import Start from '../views/Start.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import Main from '../views/UserMainpage.vue'
import AddPrinter from '../views/AddPrinter.vue'
import ListPrinter from '../views/ListPrinter.vue'
import AddSTL from '../views/AddSTL.vue'
import DirectMessage from '../views/DirectMessage.vue'

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
  },
  {
    path: '/AddPrinter',
    name: 'AddPrinter',
    component: AddPrinter
  },
  {
    path: '/ListPrinter',
    name: 'ListPrinter',
    component: ListPrinter
  },
  {
    path: '/addstl',
    name: 'AddSTL',
    component: AddSTL
  },
  {
    path: '/directmessage',
    name: 'DirectMessage',
    component: DirectMessage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
