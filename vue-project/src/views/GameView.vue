<template>
  <v-app class="hero">
    <v-container v-if="!isPortrait">


      <v-row class="justify-center">
        <v-col cols="8" class="d-flex justify-center">
          <logo v-if="gameStatus === 0" :style="{ height: '15vh', margin: '2vh 0vw 2vh 0vw' }" />
          <div v-if="gameStatus != 0" class="nums" :style="{ 'font-size': '5vw' , height:'11vh'}">
            {{ headText }}
          </div>
        </v-col>
      </v-row>


      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-img src="../assets/example.jpg" height="35vh" width="40vw" class="mx-auto" v-show="gameStatus === 0" />
          <v-img v-show="gameStatus != 0" v-bind:src="paintImg[gameStatus-1]" class="mx-auto" height="40vh" width="40vw"
            @load="timeStart" />
        </v-col>
        <v-col cols="4" class="mx-auto">
          <v-progress-linear v-show="gameStatus > 0" class="bar" height="20vh" color="white" v-model="totalTimer">
          </v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center text-center">
        <v-col>
          <v-progress-circular v-show="gameStatus > 0 && imgTimer > 5" height="4vh" color="#0000FF" :size="65"
            :width="8" model-value="100">
            <div :style="{
              'font-size': '3vh',
              color: 'black',
            }">
              {{ imgTimer }}
            </div>
          </v-progress-circular>

          <v-progress-circular v-show="gameStatus > 0 && imgTimer <= 5" height="4vh" color="#FF0000" :size="65"
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
        :style="{ 'margin-top': '1vh' }">
        <v-sheet v-for="i in answerList[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="6vh"
          width="6vh" rounded :style="{ 'margin-left': '0.5vw' }"></v-sheet>
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


    <v-container v-if="isPortrait">
    <v-row class="justify-center">
      <v-col cols="8" class="d-flex justify-center">
        <logo v-if="gameStatus === 0" :style="{ height: '15vh', margin: '2vh 0vw 2vh 0vw' }" />
        <div v-if="gameStatus != 0" class="nums d-flex align-center" :style="{ 'font-size': '10vw' , height:'15vh'}">
          {{ headText }}
        </div>
      </v-col>
    </v-row>


    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img src="../assets/example.jpg" height="20vh" width="40vw" class="mx-auto" v-show="gameStatus === 0" />
        <v-img v-show="gameStatus != 0" v-bind:src="paintImg[gameStatus-1]" class="mx-auto" height="40vh" width="40vw"
          @load="timeStart" />
      </v-col>
      <v-col cols="2" class="mx-auto">
        <v-progress-linear v-show="gameStatus > 0" class="bar"  height="10vw" color="white" v-model="totalTimer">
        </v-progress-linear>
      </v-col>
    </v-row>
    <v-row class="d-flex justify-center text-center">
      <v-col>
        <v-progress-circular v-show="gameStatus > 0 && imgTimer > 5" height="4vh" color="#0000FF" :size="65"
          :width="8" model-value="100">
          <div :style="{
            'font-size': '3vh',
            color: 'black',
          }">
            {{ imgTimer }}
          </div>
        </v-progress-circular>

        <v-progress-circular v-show="gameStatus > 0 && imgTimer <= 5" height="4vh" color="#FF0000" :size="65"
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
      :style="{ 'margin-top': '1vh' }">
      <v-sheet v-for="i in answerList[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="6vh"
        width="6vh" rounded :style="{ 'margin-left': '0.5vw' }"></v-sheet>
    </v-row>

    <v-row class="d-flex justify-center">
      <v-col cols="10" class="d-flex justify-center">
        <v-text-field v-show="gameStatus > 0" label="Enter the answer" single-line density="compact" v-model="text"
          @keydown.enter="enter"></v-text-field>

        <v-btn v-show="gameStatus == 0 && nextImg != ''" @click="startGame">Game Start!</v-btn>
      </v-col>
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
const imgTimer = ref(15);
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
const isPortrait = ref(true);


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

function checkOrientation() {
  isPortrait.value = window.screen.orientation.type === "portrait-primary";
}

function timeStart() {
  loaded.value = 1;
}

function resetImg() {
  gameStatus.value += 1;
  imgTimer.value = 15;
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

    originImg.push(response.data[i]['base_url'] + response.data[i]['img_path'])

    let tmp = response.data[i]['img_path'].split('.')
    tmp[1] = 'ani.webp'
    console.log(tmp)
    paintImg.value.push(response.data[i]['base_url'] + tmp.join('_'))
  }
  console.log(answerList.value)

  store.commit("setOrigin", originImg);
  store.commit("setPaint", paintImg.value);
  store.commit("setAnswer", answerList.value);

  checkOrientation();
  window.addEventListener("orientationchange", this.checkOrientation);
});
watch(imgTimer, (newVal) => {
  if (newVal == 0) {
    resetImg();
    correctList.value.push(false)
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