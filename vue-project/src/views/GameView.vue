<template>
  <v-app class="hero">
    <!-- 가로 모드 -->
    <v-container v-if="!isPortrait">


      <v-row class="justify-center">
        <!-- Head Text -->
        <v-col cols="8" class="d-flex justify-center">
          <!-- Save Paint! 로고 출력 -->
          <logo v-if="gameStatus === 0" :style="{ height: '15vh', margin: '2vh 0vw 2vh 0vw' }" />
          <!-- 문제 번호 / 문제 수 출력-->
          <div v-if="gameStatus != 0" class="nums" :style="{ 'font-size': '5vw', height: '11vh' }">
            {{ headText }}
          </div>
        </v-col>
      </v-row>


      <v-row>
        <v-col cols="3"></v-col>
        <!--default 이미지 출력 및 게임시작시 gif 이미지 출력-->
        <v-col cols="6">
          <v-img src="../assets/example.jpg" height="35vh" width="40vw" class="mx-auto" v-show="gameStatus === 0" />
          <v-img v-show="gameStatus != 0" v-bind:src="paintImg[gameStatus - 1]" class="mx-auto" height="40vh"
            width="100vw" @load="loaded = 1" />
        </v-col>


        <v-col cols="3" class="mx-auto">
          <v-progress-linear v-show="gameStatus > 0" class="bar" height="20vh" color="white" v-model="totalTimer" />
        </v-col>
      </v-row>


      <v-row class="d-flex justify-center text-center">
        <!-- 하나의 이미지에 대한 타이머 프로그래스 바 / 시간 초 출력 5초 이하로 남을 시 빨간색으로 표시-->
        <v-col>
          <v-progress-circular v-show="gameStatus > 0" height="4vh" :size="65" :style="{ color: progressColor }"
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


      <v-row class="d-flex justify-center" v-if="gameStatus > 0" :style="{ 'margin-top': '1vh' }">
        <!-- 정답 글자 수 표시 -->
        <v-sheet v-for="i in answerList[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="6vh"
          width="6vh" rounded :style="{ 'margin-left': '0.5vw' }"></v-sheet>
      </v-row>


      <v-row>
        <v-col cols="4"></v-col>


        <v-col cols="4" class="d-flex justify-center">
          <!-- 정답 입력 칸 -->
          <v-text-field v-show="gameStatus > 0" label="Enter the answer" single-line density="compact" v-model="text"
            @keypress.enter="enter"></v-text-field>


          <!-- 게임 시작 버튼 -->
          <v-btn v-show="gameStatus == 0" @click="startGame">Game Start!</v-btn>
        </v-col>
        <v-col cols="1">
          <v-btn v-show="imgTimer<=10" @click="showHint=true">
            Show hint!
          </v-btn>
        </v-col>
        <v-col cols="3"></v-col>
      </v-row>


      <v-row calss="d-flex justify-center">
        <!-- 정답이 틀렸는지 맞았는지 표시 -->
        <div v-show="wrongTimer > 0" class="mx-auto">
          <wrong />
        </div>
        <div v-show="rightTimer > 0" class="mx-auto">
          <right />
        </div>
      </v-row>
    </v-container>


    <!-- 세로 모드 -->
    <v-container v-if="isPortrait">


      <v-row class="d-flex justify-center" v-if="gameStatus == 0">
        <!-- save paint logo 출력 -->
        <v-col cols="8" class="d-flex justify-center">
          <logo :style="{ height: '15vh', margin: '2vh 0vw 2vh 0vw' }" />
        </v-col>
      </v-row>


      <!-- 문제 번호 출력 -->
      <v-row class="d-flex justify-center" v-if="gameStatus != 0">
        <v-col cols="8" class="d-flex justify-center">
          <div v-if="gameStatus != 0" class="nums d-flex align-center" :style="{ 'font-size': '10vw', height: '7vh' }">
            {{ headText }}
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-progress-linear v-show="gameStatus > 0" class="mobile-bar" height="10vw" color="white"
          v-model="totalTimer" />
      </v-row>


      <!-- default 이미지 및 gif 게임 이미지 출력 -->
      <v-col cols="12">
        <v-img src="../assets/example.jpg" height="45vh" width="100vw" class="mx-auto" v-show="gameStatus === 0" />
        <v-img v-show="gameStatus != 0" v-bind:src="paintImg[gameStatus - 1]" class="mx-auto" height="45vh"
          width="100vw" @load="loaded = 1" />
      </v-col>


      <v-row class="d-flex justify-center text-center">
        <!-- 하나의 이미지에 대한 타이머 프로그래스 바 / 시간 초 출력 5초 이하로 남을 시 빨간색으로 표시-->
        <v-col>
          <v-progress-circular v-show="gameStatus > 0" height="4vh" :size="65" :style="{ color: progressColor }"
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


      <v-row class="d-flex justify-center" v-if="gameStatus > 0 
        " :style="{ 'margin-top': '1vh' }">
        <!-- 정답 글자 수 표시 -->
        <v-sheet v-for="i in answerList[gameStatus - 1].length" :key="{ i }" color="white" elevation="1" height="6vh"
          width="6vh" rounded :style="{ 'margin-left': '0.5vw', 'margin-bottom': '1vh' }"></v-sheet>
      </v-row>

      <v-row class="d-flex justify-center">
        <!-- 정답 입력 칸 -->
        <v-col cols="9" class="d-flex justify-center">
          <v-text-field @keydown.enter="enter" v-show="gameStatus > 0" label="Enter the answer" single-line density="compact" v-model="text"
            ></v-text-field>
          <!-- 게임 시작 버튼 -->
          <v-btn v-show="gameStatus == 0" @click="startGame">Game Start!</v-btn>
        </v-col>
        <v-col cols="2" v-show="gameStatus>0">
        <v-btn @click="enter">입력</v-btn>
        </v-col>
      </v-row>


      <v-row calss="d-flex justify-center">
        <!-- 정답이 틀렸는지 맞았는지 표시 -->
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


/**
 * @property {Number} imgTimer 하나의 이미지에 대한 시간 표시 (15초 -> 0초)
 * @property {Number} TotalTimer 전체 이미지에 대한 시간 표시 (0% -> 100%)
 * @property {Number} rightTimer  정답 입력시 맞았다는 표시 (2초 -> 0초)
 * @property {Number} wrongTimer 틀린 정답 입력시 틀렸다는 표시 (2초 > 0초)
 * @property {Number} gameStatus 게임 상황 표시 (0=시작전 1~9: 문제 번호 10: 게임 종료)
 * @property {String} headText 게임시 위에 표시되는 head 부분의 text
 * @property {String} text 정답 입력칸에 유저가 입력한 text
 * @property {Array<String>} answerList 서버에서 받은 문제의 정답 배열
 * @property {Array<String>} paintImg 서버에서 받은 문제의 gif url
 * @property {Router}  router 다른 페이지 이동을 위한 라우팅 객체
 * @property {Store} store vuex storage 접근을 위한 객체
 * @property {Number} loaded 화면에 이미지가 로딩되었는지를 확인하기 위한 객체, 타이머 시작을 위해 쓰임(0=로딩안됨 1=로딩됨)
 * @property {Array<Boolean>} correctList 정답을 맞췄는지 못맞췄는지를 확인하기 위한 객체
 * @property {Boolean} isPortrait 화면 모드 (세로모드 = true 가로모드 = false)
 * @property {String} progressColor 이미지당 시간을 나타내는 프로그래스 바 색 지정 (5초 이하는 빨간색 나머지 파란색)
 */
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
const correctList = ref([])
const isPortrait = ref(true);
const progressColor = ref("#0000FF")
const showHint = ref(false)


/**
 * 각각의 타이머에 대한 시간 체크 함수 1/1000 단위
 * @function setInterval
 */
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


/**
 * device의 가로모드 세로모드를 확인하기 위한 함수
 * @function checkOrientation
 */
function checkOrientation() {
  isPortrait.value = window.screen.orientation.type === "portrait-primary";
}

function filterLetters(str) {
  return str.replace(/[0-9]/g, '');
}

/**
 * 게임 화면이 넘어갈 때 마다 새로운 텍스트및 이미지를 지정해주는 함수
 * @function resetImg
 * gameStatus의 증가로 다음 이미지를 지정
 * 이미지 타이머 및 유저 입력 초기화
 * 해드 텍스트 변경
 */
function resetImg() {
  gameStatus.value += 1;
  imgTimer.value = 15;
  headText.value = `${gameStatus.value}/9`;
  text.value = "";
}


/**
 * 게임 시작 버튼을 누르면 게임이 시작되는 이벤트 발생 및 전체 타이머 초기화
 * @function startGame
 */
function startGame() {
  resetImg();
  totalTimer.value = 0;
}


/**
 * 사용자가 정답칸에 입력을 했을 시 발생하는 이벤트
 * @function enter
 * 정답을 맞췄을 때 게임이 마지막 이미지를 보고 있는 상태였다면 다음 페이지에 필요한 정보를 저장하고 이동
 * 그 외 정답을 맞췄을 때는 타이머 초기화(정답 표시) 및 다음 화면 전환을 위한 resetImg 실행
 * 정답이 틀렸다면 타이머 초기화(오답 표시) 및 유저 입력 초기화 
 */
function enter() {
  if (text.value == answerList.value[gameStatus.value - 1]) {
    loaded.value = 0
    correctList.value.push(true)
    showHint.value=false
    if (gameStatus.value === 9) {
      store.commit("setCleartime", totalTimer);
      store.commit("setCorrect", correctList.value)
      gameOver()
      router.push({ path: "/rank" });
    }
    else {
      if (wrongTimer.value > 0) {
        wrongTimer.value = 0;
      }
      rightTimer.value = 2;
      resetImg();
    }
  } else {
    if (rightTimer.value > 0) {
      rightTimer.value = 0;
    }
    wrongTimer.value = 2;
    text.value = "";
  }
}


/**
 * game이 끝나면 서버에 메타 정보를 보내는 함수
 * @function gameover
 */
async function gameOver() {
  const headers = { "Content-Type": "application/json" };
  const params = { category: store._state.data.category, img_paths: store._state.data.imgPath, correct_list: store._state.data.correctList };

  let response = await axios.post(
    "http://34.64.169.197/api/v1/game/gameover",
    params,
    { headers }
  );
}


const handleOrientationChange = () => {
  if (window.innerHeight <= 480 && screen.orientation.type.startsWith('landscape')) {
    alert('Please use portrait mode on mobile devices.')
  }
}


/**
 * 화면이 마운트 될 시 필요한 정보를 서버로 부터 가져오고 저장 및 화면의 portrait 여부 구별
 * @function onMounted
 */
onMounted(async () => {
  const headers = { "Content-Type": "application/json" };
  const params = { category: store._state.data.category };
  let response = await axios.post(
    "http://34.64.169.197/api/v1/game/gamestart",
    params,
    { headers }
  );

  let originImg = []
  let imgPath = []

  for (let i = 0; i < 9; i++) {
    answerList.value.push(filterLetters(response.data[i]['label']))

    originImg.push(response.data[i]['base_url'] + response.data[i]['img_path'])
    imgPath.push(response.data[i]['img_path'])

    let tmp = response.data[i]['img_path'].split('.')
    tmp[1] = 'ani.webp'
    paintImg.value.push(response.data[i]['base_url'] + tmp.join('_'))
  }
  console.log(answerList.value)

  store.commit("setOrigin", originImg);
  store.commit("setPaint", paintImg.value);
  store.commit("setAnswer", answerList.value);
  store.commit('setPath', imgPath)

  checkOrientation();
  window.addEventListener("orientationchange", checkOrientation);
});


/**
 * 타이머 시간에 끝남에 따라 발생하는 이벤트 지정
 * @function watch
 */
watch(imgTimer, (newVal) => {
  if (newVal == 0) {
    correctList.value.push(false)
    showHint.value=false
    if (gameStatus.value === 9) {
      store.commit("setCleartime", totalTimer);
      store.commit("setCorrect", correctList.value)
      gameOver()
      router.push({ path: "/rank" });
    }
    else{
      resetImg()
    }
  }
  if (newVal <= 5) {
    progressColor.value = "#FF0000"
  }
  else {
    progressColor.value = "#0000FF"
  }
});
watch(totalTimer, (newVal) => {
  if (Math.floor(newVal) == 100) {
    store.commit("setCleartime", 100);
    store.commit("setCorrect", correctList.value)
    gameOver()
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
  background: linear-gradient(to right, #E54040 0%, #FFA63A 16%, #DCFF3F 32%, #6CFF3F 48%, #3FA2FF 64%, #A53FFF 80%, #FF3FC9 100%);
  border-radius: 30px;
}


.mobile-bar {
  transform: rotate(180deg);
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
  font-family: 'num';
  src: url('../fonts/Lobster-Regular.ttf')
}

.nums {
  font-family: 'num';
  font-size: 4rem;
}
</style>