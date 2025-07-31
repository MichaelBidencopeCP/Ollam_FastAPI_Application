import { createRouter, createWebHistory } from 'vue-router'
import homeView from '@/views/homeView.vue'
import chatView from '@/views/chatView.vue'
import notFoundView from '@/views/notFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: homeView
    },
    {
      path: '/chat',
      name: 'chat',
      component: chatView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: notFoundView
    }
  ],
})

export default router
