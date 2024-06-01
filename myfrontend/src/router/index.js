import { createRouter, createWebHistory } from 'vue-router'
import ProductsView from '../views/ProductsView.vue'

const routes = [
  {
    path: '/products',
    name: 'products',
    component: ProductsView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/home',
    name: 'home',
    component: ()=>import('@/views/HomeView.vue')
  },
  {
    path:'/services',
    name:'services',
    component: ()=>import('@/views/ServicesView.vue')
  },
  
  {path:'/assets',
    name:'assets',
    component: ()=>import('@/views/AssetsView.vue')
  },
  {
    path:'/login',
    name:'login',
    component: ()=>import('@/views/LoginView.vue')
  },
  {
    path:'/register',
    name:'register',
    component: ()=>import('@/views/RegisterView.vue')
  },
  {
    path:'/sales',
    name:'sales',
    component: ()=>import('@/views/SalesView.vue')
  },
  {
    path:'/sale/new',
    name:'sale-new',
    component: ()=>import('@/views/SalesForm.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
