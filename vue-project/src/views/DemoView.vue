<template>
    <v-app class="hero">
        <v-container>
            <v-row class="justify-center">
                <logo v-if='gameStatus===0' :style="{ height: '20vh', width: '40vw' }" />
                <div v-if="gameStatus!=0" class="nums" >{{ headText }}</div>
            </v-row>
            <v-row class="d-flex mt-8">
                <v-col cols="4"></v-col>
                <v-col cols="4">
                    <v-img src="../assets/example.jpg" height="40vh" width="40vw" class="mx-auto"
                        v-show="gameStatus === 0" />
                    <v-img v-show="gameStatus != 0" v-bind:src="currentImg" class="mx-auto" height="40vh" width="40vw"
                        @load="timeStart" />
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
            <v-row class="d-flex justify-center mt-10">
                <v-col cols="4"></v-col>
                <v-text-field v-show="gameStatus > 0" width="10px" label="Enter the answer" single-line
                    density="compact" v-model="text" @keydown.enter="enter"></v-text-field>
                <v-btn v-show="gameStatus == 0 && nextImg != ''" @click="startGame">Game Start!</v-btn>
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
const currentImg = ref("");
const nextImg = ref("");
const answer = ref([]);
const router = useRouter();
const store = useStore();
const loaded = ref(0);
const rank = "A";
const imgList = ref([]);
const correctAnswers = ref(0);
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
    imgTimer.value = 0;
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
    if (gameStatus.value === 9) {
        store.commit("setRank", rank);
        store.commit("setCleartime", totalTimer);
        store.commit("setCorrectanswers", correctAnswers);
        router.push({ path: "/rank" });

    }
    if (text.value == answer.value[gameStatus.value - 1]) {
        correctAnswers.value = correctAnswers.value + 1;
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
    if (newVal == 100) {
        resetImg();
    }
});
watch(totalTimer, (newVal) => {
    if (Math.floor(newVal) == 100) {
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
    src:url('../fonts/Lobster-Regular.ttf')
}

.nums{
    font-family: 'num';
    font-size: 4rem;
}
</style>