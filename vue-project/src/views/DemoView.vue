<template>
  <v-app class="hero">
    <v-container>
      <v-row class="d-flex justify-center mt-16">
        <div
          :style="{ 'font-size': '30px', color: 'black' }"
          class="d-flex justify-center align-center"
        >
          {{ headText }}
        </div>
      </v-row>
      <v-row class="d-flex mt-16">
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-img
            src="../assets/example.jpg"
            height="350"
            width="350"
            class="mx-auto"
            v-show="gameStatus === 0"
          />
          <v-img
            v-show="gameStatus != 0"
            v-bind:src="currentImg"
            class="mx-auto"
            height="500"
            width="500"
            @load="timeStart"
          />
        </v-col>
        <v-col cols="4">
          <v-progress-linear
            v-show="gameStatus > 0"
            class="rotate"
            height="20"
            width="40"
            v-model="totalTimer"
          >
          </v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center mt-8">
        <v-col cols="4">
          <v-progress-linear
            v-show="gameStatus > 0"
            v-model="imgTimer"
            height="7"
            rounded
            color="indigo"
          ></v-progress-linear>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center mt-10">
        <v-col cols="2"></v-col>
        <v-text-field
          v-show="gameStatus > 0"
          class="text"
          clearable
          hide-details="auto"
          label="Enter the answer"
          single-line
          density="compact"
          v-model="text"
          @keydown.enter="enter"
        ></v-text-field>
        <v-btn v-show="gameStatus == 0 && nextImg != ''" @click="startGame"
          >Game Start!</v-btn
        >
        <v-col cols="2"></v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";

const imgTimer = ref(100);
const totalTimer = ref(100);
const gameStatus = ref(0);
const headText = ref("Save Paint!");
const text = ref("");

const currentImg = ref("");
const nextImg = ref("");
const answer = ref([]);

const router = useRouter();
const store = useStore();
const loaded = ref(0);
const rank = "A";
const imgList = ref([]);

setInterval(() => {
  if (loaded.value == 1) {
    imgTimer.value = imgTimer.value - 1;
  }
}, 150);
setInterval(() => {
  if (loaded.value == 1) {
    totalTimer.value = totalTimer.value - 1;
  }
}, 1800);

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
  imgTimer.value = 100;
  headText.value = `${gameStatus.value}/9`;
  text.value = "";
  currentImg.value = nextImg.value;
  callNext();
}
function startGame() {
  resetImg();
  totalTimer.value = 100;
}
function enter() {
  if (gameStatus.value === 9) {
    store.commit("setRank", rank);
    router.push({ path: "/rank" });
  }
  if (text.value == answer.value[gameStatus.value - 1]) {
    resetImg();
  } else {
    text.value = "";
  }
}

onMounted(async () => {
  const query = router.currentRoute.value.query;
  const params = { category: query.category, mode: query.mode };
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
  if (newVal == 0) {
    router.push({ path: "/rank", props: { rank: "A" } });
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

.rotate {
  transform: rotate(270deg);
  border-radius: 12px;
  margin-top: 150px;
}

.text {
  margin-left: 300px;
  margin-right: 300px;
}
</style>
