import { createRouter, createWebHistory } from 'vue-router'
import startview from '../views/StartView.vue'
import selectview from '../views/SelectView.vue'
import gameview from '../views/GameView.vue'
import descriptionview from '../views/DescriptionView'
import resultview from '../views/ResultView'

const routes = [
  {
    path: '/',
    name: 'start',
    component: startview
  },
  {
    path: '/select',
    name: 'select',
    component: selectview
  },
  {
    path:'/game',
    name:'game',
    component: gameview
  },
  {
    path:'/description',
    name:'description',
    component: descriptionview
  },
  {
    path:'/result',
    name:'result',
    component: resultview
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
