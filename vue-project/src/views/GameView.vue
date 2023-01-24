<template>
    <v-app>
        <v-container>
            <v-row class="d-flex justify-center mt-16">
                <div :style="{ 'font-size': '30px', 'color': 'black' }" class="d-flex justify-center align-center">
                    {{ headText }}</div>
            </v-row>
            <v-row class="d-flex mt-16">
                <v-col cols="4"></v-col>
                <v-col cols="4">
                    <v-img src="../assets/example.jpg" height="350" width="350" class="mx-auto"
                        v-show="gameStatus === 0" />
                    <v-img v-if="gameStatus != 0" :src="currentImg" class="mx-auto" height="350" width="350"
                        @load="timeStart" />
                </v-col>
                <v-col cols=4>
                    <v-progress-linear v-show="gameStatus > 0" class="rotate" height="20" width="40"
                        v-model="totalTimer">
                    </v-progress-linear>
                </v-col>
            </v-row>
            <v-row class="d-flex justify-center mt-8">
                <v-col cols=4>
                    <v-progress-linear v-show="gameStatus > 0" v-model="imgTimer" height="7" rounded
                        color="indigo"></v-progress-linear>
                </v-col>
            </v-row>
            <v-row class="d-flex justify-center mt-10">
                <v-text-field v-show="gameStatus > 0" class="text" clearable hide-details="auto" height="10px"
                    label="Enter the answer" single-line density="compact" v-model="text"
                    @keydown.enter="enter"></v-text-field>
                <v-btn v-show="gameStatus == 0" @click="startGame">Game Start!</v-btn>
            </v-row>
        </v-container>
    </v-app>
</template>

<script setup>
import { ref, onMounted, watch, computed, } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from "vuex";
import axios from 'axios';
const imgTimer = ref(100)
const totalTimer = ref(100)
const gameStatus = ref(0)
const headText = ref('Save Paint!')
const text = ref('')
const originImg = ref([])
const paintImg = ref([])
const answer = ref([])
const router = useRouter()
const store = useStore()
const result = ref([])
const loaded = ref(0)
const rank = 'A'
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
    loaded.value = 1
}
const currentImg = computed(function () {
    if (gameStatus.value > 0 && paintImg.value.length > 0) {
        return `data:image/gif;base64, ${paintImg.value[gameStatus.value - 1]}`
    }
    else {
        return null
    }
});
function resetImg() {
    gameStatus.value += 1
    imgTimer.value = 100
    headText.value = `${gameStatus.value}/9`
    text.value = ''
}
function startGame() {
    resetImg()
    totalTimer.value = 100
}
function enter() {
    if (gameStatus.value === 8) {
        store.commit('setRank', rank)
        router.push({ path: '/rank' })
    }
    if (text.value == answer.value[gameStatus.value - 1]) {
        resetImg()
    }
    else {
        text.value = ''
    }
}
onMounted(async () => {
    const headers = { 'Content-Type': 'application/json' }
    const query = router.currentRoute.value.query
    const params = { category: query.category, mode: query.mode }
    let response = await axios.post('http://127.0.0.1:8000/api/v1/game/gamestart', params, { headers })
    originImg.value = response.data.origin_img
    paintImg.value = response.data.paint_img
    answer.value = response.data.answer
    result.value = response.data.result_img
    store.commit('setOrigin', response.data.origin_img)
    store.commit('setPaint', response.data.paint_img)
    store.commit('setAnswer', response.data.answer)
    store.commit('setResult', response.data.result_img)
})
watch(imgTimer, (newVal) => {
    if (newVal == 0) {
        resetImg()
    }
})
watch(totalTimer, (newVal) => {
    if (newVal == 0) {
        router.push({ path: '/rank', props: { rank: 'A' } })
    }
})
</script>

<style scoped>
.hero {
    background: url('../assets/back.jpg');
    background-size: cover;
    height: 100vh;
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
