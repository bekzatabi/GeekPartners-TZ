import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '@/pages/MainPage'
import OrdersPage from '@/pages/OrdersPage'
import OrderDetail from '@/components/OrderDetail'

const routes = [
  {
    path: '/',
    component: MainPage,
  },
  {
    path: '/orders',
    component: OrdersPage,
  },
  {
    path: '/orders/:orderId',
    component: OrderDetail,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
