import { createRouter, createWebHistory } from 'vue-router'
import startview from '../views/StartView.vue'
import selectview from '../views/SelectView.vue'
import gameview from '../views/GameView.vue'
import descriptionview from '../views/DescriptionView'
import resultview from '../views/ResultView'
import transformview from '../views/TransformView.vue'
import rankview from '../views/RankView'
import leaderboard from '../views/LeaderBoard'
import store from '../store/store'

const routes = [
  {
    path: "/",
    name: "start",
    component: startview,
  },
  {
    path: "/select",
    name: "select",
    component: selectview,
  },
  {
    path: "/game",
    name: "game",
    component: gameview,
    beforeEnter: (to, from, next) => {
      if (store.state.category === '') {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: "/description",
    name: "description",
    component: descriptionview,
  },
  {
    path: "/result",
    name: "result",
    component: resultview,
    beforeEnter: (to, from, next) => {
      if (store.state.originImg.length === 0) {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: "/transform",
    name: "transform",
    component: transformview,
  },
  {
    path:'/rank',
    name:'rank',
    component: rankview,
    beforeEnter: (to, from, next) => {
      if (store.state.score === 0) {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: "/leaderboard",
    name: "leaderboard",
    component: leaderboard
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'
  }
];



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  mode: 'history',
});


export default router;
