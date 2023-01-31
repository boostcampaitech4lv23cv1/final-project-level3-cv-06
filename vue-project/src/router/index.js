import { createRouter, createWebHistory } from 'vue-router'
import startview from '../views/StartView.vue'
import selectview from '../views/SelectView.vue'
import gameview from '../views/GameView.vue'
import descriptionview from '../views/DescriptionView'
import resultview from '../views/ResultView'
import detailview from '../views/DetailView'
import transformview from '../views/TransformView'
import rankview from '../views/RankView'
import demoview from '../views/DemoView'
import demoresult from '../views/DemoResult'
import demodetail from '../views/DemoDetail'
import leaderboard from '../views/LeaderBoard'


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
  },
  {
    path: "/detail",
    name: "detail",
    component: detailview,
  },
  {
    path: "/transform",
    name: "transform",
    component: transformview,
  },
  {
    path:'/rank',
    name:'rank',
    component: rankview
  },

  {
    path: "/demo",
    name: "demo",
    component: demoview,
  },
  {
    path: "/demoresult",
    name: "demoresult",
    component: demoresult,
  },
  {
    path: "/demodetail",
    name: "demodetail",
    component: demodetail,
  },
  {
    path: "/leaderboard",
    name: "leaderboard",
    component: leaderboard
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
