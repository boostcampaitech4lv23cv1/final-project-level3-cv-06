<template>
  <v-app class="hero">
    <v-container>


      <v-row class="justify-center">
        <v-col cols="10" class="d-flex justify-center">
          <logo v-if="gameStatus === 0" :style="{ height: '15vh', margin: '2vh 0vw 2vh 0vw' }" />
          <div v-if="gameStatus != 0" class="nums" :style="{ 'font-size': '5vw' }">
            {{ headText }}
          </div>
        </v-col>
      </v-row>


      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-img src="../assets/example.jpg" height="40vh" width="40vw" class="mx-auto" v-show="gameStatus === 0" />
          <v-img v-show="gameStatus != 0" v-bind:src="currentImg" class="mx-auto" height="40vh" width="40vw"
            @load="timeStart" />
        </v-col>
        <v-col cols="4" class="mx-auto">
          <v-progress-linear v-show="gameStatus > 0" class="bar" height="20vh" color="white" v-model="totalTimer">
          </v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center text-center">
        <v-col>
          <v-progress-circular v-show="gameStatus > 0 && imgTimer > 5" height="5vh" color="#0000FF" :size="65"
            :width="8" model-value="100">
            <div :style="{
              'font-size': '3vh',
              color: 'black',
            }">
              {{ imgTimer }}
            </div>
          </v-progress-circular>

          <v-progress-circular v-show="gameStatus > 0 && imgTimer <= 5" height="5vh" color="#FF0000" :size="65"
            :width="8" model-value="100">
            <div :style="{
              'font-size': '3vh',
              color: 'black',
            }">
              {{ imgTimer }}
            </div>
          </v-progress-circular>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center" v-if="(gameStatus != 0) & (gameStatus != 10)"
        :style="{ 'margin-top': '3vh' }">
        <v-sheet v-for="i in answer[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="7vh"
          width="6vh" rounded :style="{ 'margin-left': '1vw' }"></v-sheet>
      </v-row>

      <v-row>
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
const imgTimer = ref(100);
const totalTimer = ref(0);
const rightTimer = ref(0);
const wrongTimer = ref(0);
const gameStatus = ref(0);
const headText = ref("Save Paint!");
const text = ref("");
const currentImg = ref("");
const nextImg = ref("");
const answer = ref([]);
const router = useRouter();
const store = useStore();
const loaded = ref(0);
const imgList = ref([]);
const correctAnswers = ref(0);

setInterval(() => {
  if (loaded.value == 1) {
    imgTimer.value = imgTimer.value - 1;
  }
}, 1000);
setInterval(() => {
  if (loaded.value == 1) {
    totalTimer.value = totalTimer.value + 0.1;
  }
}, 100);
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
const callNext = async () => {
  if (gameStatus.value > 8) {
    return;
  }
  const response = await axios.post(
    "http://127.0.0.1:8000/api/v1/game/paint",
    { path: imgList.value[gameStatus.value] },
    {
      responseType: "arraybuffer",
    }
  );
  const chunks = new Uint8Array(response.data);
  let total = chunks.length;
  let chunksArr = new Array();
  let offset = 0;
  for (let i = 0; i < total; i += 1024) {
    chunksArr.push(chunks.slice(offset, offset + 1024));
    offset += 1024;
  }
  const gifBlob = new Blob(chunksArr, { type: "image/gif" });
  nextImg.value = URL.createObjectURL(gifBlob);
};
function resetImg() {
  gameStatus.value += 1;
  imgTimer.value = 15;
  headText.value = `${gameStatus.value}/9`;
  text.value = "";
  currentImg.value = nextImg.value;
  callNext();
}
function startGame() {
  resetImg();
  totalTimer.value = 0;
}

function enter() {
  if (text.value == answer.value[gameStatus.value - 1]) {
    correctAnswers.value = correctAnswers.value + 1;
    if (wrongTimer.value > 0) {
      wrongTimer.value = 0;
    }
    rightTimer.value = 2;

    if (gameStatus.value === 9) {
      store.commit("setCleartime", totalTimer);
      store.commit("setCorrectanswers", correctAnswers);
      router.push({ path: "/rank" });
      loaded.value = 0;
    }

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
  const params = {
    category: store._state.data.category,
    mode: store._state.data.mode,
  };
  const headers = { "Content-Type": "application/json" };
  const response1 = await axios.post(
    "http://127.0.0.1:8000/api/v1/game/gamestart",
    params,
    headers
  );
  imgList.value = response1.data.img_list;
  answer.value = response1.data.answer_list;
  store.commit("setPath", response1.data.img_list);
  console.log(answer.value);
  store.commit("setAnswer", answer.value);

  const response = await axios.post(
    "http://127.0.0.1:8000/api/v1/game/paint",
    { path: imgList.value[0] },
    {
      headers: { "Content-Type": "application/json" },
      responseType: "arraybuffer",
    }
  );
  const chunks = new Uint8Array(response.data);
  let total = chunks.length;
  let chunksArr = new Array();
  let offset = 0;
  for (let i = 0; i < total; i += 1024) {
    chunksArr.push(chunks.slice(offset, offset + 1024));
    offset += 1024;
  }
  const gifBlob = new Blob(chunksArr, { type: "image/gif" });
  nextImg.value = URL.createObjectURL(gifBlob);
});
watch(imgTimer, (newVal) => {
  if (newVal == 0) {
    resetImg();
  }
});
watch(totalTimer, (newVal) => {
  if (Math.floor(newVal) == 100) {
    store.commit("setCleartime", 100);
    store.commit("setCorrectanswers", correctAnswers);
    router.push({ path: "/rank" });
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
  background: linear-gradient(to right,
      #e54040 0%,
      #ffa63a 16%,
      #dcff3f 32%,
      #6cff3f 48%,
      #3fa2ff 64%,
      #a53fff 80%,
      #ff3fc9 100%);
  border-radius: 30px;
}

@font-face {
  font-family: "num";
  src: url("../fonts/Lobster-Regular.ttf");
}

@media only screen and (max-height: 480px) {
  .nums {
    font-family: "num";
    font-size: 2rem;
  }
}

@media only screen and (min-height: 480px) {
  .nums {
    font-family: "num";
    font-size: 4rem;
  }
}
</style>
