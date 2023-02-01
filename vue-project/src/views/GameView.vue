<template>
  <v-app class="hero">
    <v-container>
      <v-row class="justify-center">
        <logo v-if='gameStatus === 0' :style="{ height: '20vh', width: '40vw' }" />
        <div v-if="gameStatus != 0" class="nums">{{ headText }}</div>
      </v-row>
      <v-row class="d-flex justify-center mt-8" v-if="gameStatus != 0 & gameStatus != 10">
        <v-sheet v-for="(i) in answer[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="7vh"
          width="6vh" rounded :style="{ 'margin-left': '0.2vw' }"></v-sheet>
      </v-row>
      <v-row class="d-flex mt-8">
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-img src="../assets/example.jpg" height="40vh" width="40vw" class="mx-auto" v-show="gameStatus === 0" />
          <v-img v-show="gameStatus != 0" v-bind:src="paintImg[gameStatus - 1]" class="mx-auto" height="40vh"
            width="40vw" @load="timeStart" />
        </v-col>
        <v-col cols="4" class="mx-auto">
          <v-progress-linear v-show="gameStatus > 0" class="rotate bar" height="20vh" color="white"
            v-model="totalTimer">
          </v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center mt-8">
        <v-col cols="4">
          <v-progress-linear v-show="gameStatus > 0" v-model="imgTimer" height="20vh" rounded
            color="white"></v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="mt-10">
        <v-col cols="4"></v-col>
        <v-col cols="4" class="d-flex justify-center">
          <v-text-field v-show="gameStatus > 0" label="Enter the answer" single-line density="compact" v-model="text"
            @keydown.enter="enter"></v-text-field>
          <v-btn v-show="gameStatus == 0 && nextImg != ''" @click="startGame">Game Start!</v-btn>
        </v-col>
        <v-col cols="4"></v-col>
      </v-row>
      <v-row calss="d-flex justify-center">
        <div v-show="wrongTimer > 0" class="mx-auto">
          <wrong />
        </div>
        <div v-show="rightTimer > 0" class="mx-auto">
          <right />
        </div>
      </v-row>
    </v-container>
  </v-app>
</template>
<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";
import logo from "../svg/logoView.vue";
import wrong from "../svg/wrongAnswer.vue";
import right from "../svg/rightAnswer.vue";
const imgTimer = ref(0);
const totalTimer = ref(0);
const rightTimer = ref(0);
const wrongTimer = ref(0);
const gameStatus = ref(0);
const headText = ref("Save Paint!");
const text = ref("");
const answerList = ref([]);
const paintImg = ref([]);
const router = useRouter();
const store = useStore();
const loaded = ref(0);
const rank = "A";
const correctList = ref([])


setInterval(() => {
  if (loaded.value == 1) {
    imgTimer.value = imgTimer.value + 1;
  }
}, 150);
setInterval(() => {
  if (loaded.value == 1) {
    totalTimer.value = totalTimer.value + 0.1;
  }
}, 90);
setInterval(() => {
  if (rightTimer.value > 0) {
    rightTimer.value = rightTimer.value - 1;
  }
}, 1000);
setInterval(() => {
  if (wrongTimer.value > 0) {
    wrongTimer.value = wrongTimer.value - 1;
  }
}, 1000);
function timeStart() {
  loaded.value = 1;
}

function resetImg() {
  gameStatus.value += 1;
  imgTimer.value = 0;
  headText.value = `${gameStatus.value}/9`;
  text.value = "";
}
function startGame() {
  resetImg();
  totalTimer.value = 0;
}
function enter() {
  if (gameStatus.value === 9) {
    store.commit("setRank", rank);
    store.commit("setCorrect", correctList.value)
    router.push({ path: "/rank" });
  }
  if (text.value == answerList.value[gameStatus.value - 1]) {
    correctList.value.push(true)
    if (wrongTimer.value > 0) {
      wrongTimer.value = 0;
    }
    rightTimer.value = 2;
    resetImg();
  } else {
    if (rightTimer.value > 0) {
      rightTimer.value = 0;
    }
    wrongTimer.value = 2;
    text.value = "";
  }
}
onMounted(async () => {
  const headers = { "Content-Type": "application/json" };
  const params = { category: store._state.data.category };
  let response = await axios.post(
    "http://34.64.169.197/api/v1/game/gamestart",
    params,
    { headers }
  );

  let originImg = []

  for (let i = 0; i < 9; i++) {
    answerList.value.push(response.data[i]['label'])

    originImg.push('https://storage.googleapis.com/image_cloud_demo/' + response.data[i]['img_path'])

    let tmp = response.data[i]['img_path'].split('_')
    tmp[1] = 'ani.webp'
    paintImg.value.push('https://storage.googleapis.com/image_cloud_demo/' + tmp.join('_'))
  }
  console.log(answerList.value)

  store.commit("setOrigin", originImg);
  store.commit("setPaint", paintImg.value);
  store.commit("setAnswer", answerList.value);

});
watch(imgTimer, (newVal) => {
  if (newVal == 100) {
    resetImg();
    correctList.value.push(false);
  }
});
watch(totalTimer, (newVal) => {
  if (Math.floor(newVal) == 100) {
    router.push({ path: "/rank", props: { rank: "A" } });
    store.commit("setCorrect", correctList.value)
  }
});
</script>
<style scoped>
.hero {
  background: url("../assets/canvas.jpg");
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
}

.text {
  margin-left: 300px;
  margin-right: 300px;
}

.bar {
  transform: rotate(90deg);
  margin-top: 17vh;
  background: linear-gradient(to right, #E54040 0%, #FFA63A 16%, #DCFF3F 32%, #6CFF3F 48%, #3FA2FF 64%, #A53FFF 80%, #FF3FC9 100%);
  border-radius: 30px;
}

@font-face {
  font-family: 'num';
  src: url('../fonts/Lobster-Regular.ttf')
}

.nums {
  font-family: 'num';
  font-size: 4rem;
}
</style>