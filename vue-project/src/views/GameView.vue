<template>
    <v-app>
    <v-container>
        <v-row class="d-flex justify-center mt-16">
            <div :style="{ 'font-size': '30px', 'color': 'black' }" class="d-flex justify-center align-center">{{head_text}}</div>
        </v-row>
        <v-row class="d-flex mt-16">
            <v-col cols="4"></v-col>
            <v-col cols="4">
                <v-img src="../assets/example.jpg" height="350" width="350" class="mx-auto" v-show="game_status===0" />
                <v-img class="mx-auto" height="350" width="350" v-show="game_status!=0" :src="currentImg" @load="timeStart"/>
            </v-col>
            <v-col cols=4>
            <v-progress-linear
                    v-show="game_status>0"
                    class="rotate"
                    height="20"
                    width="40"
                    v-model="total_timer">
            </v-progress-linear>
            </v-col>
        </v-row>
        <v-row class="d-flex justify-center mt-8">
            <v-col cols=4>
                <v-progress-linear v-show="game_status>0" v-model="img_timer" height="7" rounded color="indigo" ></v-progress-linear>
            </v-col>
        </v-row>
        <v-row class="d-flex justify-center mt-10">
                <v-text-field v-show="game_status>0"
                    class="text"
                    clearable
                    hide-details="auto"
                    height="10px"
                    label="Enter the answer"
                    single-line
                    density="compact"
                    v-model="text"
                    @keydown.enter="enter"
                ></v-text-field>
                <v-btn v-show="game_status==0" @click="startGame">Game Start!</v-btn>
        </v-row>
    </v-container>
    <!-- <img :src="'data:image/gif;base64,'+test"/> -->
    </v-app>

</template>

<script setup>
    import { ref,onMounted,computed,watch } from 'vue'
    import { useRouter } from 'vue-router';
    import { useStore } from "vuex";
    import axios from 'axios';

    const img_timer=ref(100)
    const total_timer=ref(100)
    const game_status=ref(0)
    const head_text=ref('Save Paint!')
    const text=ref('')
    const originImg=ref([])
    const paintImg=ref([])
    const answer=ref([])
    const router = useRouter()
    const store = useStore()
    const result = ref([])
    const loaded = ref(0)

    setInterval(() => {
            if(loaded.value==1){
                img_timer.value = img_timer.value - 1;
            }
    }, 300);
    
    setInterval(() => {
            if(loaded.value==1){
                total_timer.value = total_timer.value-1;
            }
    }, 1800);


    function timeStart(){
        loaded.value=1
    }
    
    const currentImg = computed(function(){
            if (game_status.value>0 && paintImg.value.length>0 ){
                return `data:image/gif;base64, ${paintImg.value[game_status.value-1]}`
            }
            else{
                return null
            }
        });

    function startGame(){
        game_status.value+=1
        img_timer.value=100
        total_timer.value=100
    }

    function enter(){
        if (text.value==answer.value[game_status.value-1]){
            text.value=''
            game_status.value+=1
            img_timer.value=100
        }
        if (game_status.value===10){
            router.push({path: '/result',props:{originImg:originImg.value,paintImg:paintImg.value,answer:answer.value}})
        }
    }
    onMounted(async () => {
        const headers={ 'Content-Type': 'application/json' }
        const query=router.currentRoute.value.query
        const params= {category:query.category,mode:query.mode}
        let response = await axios.post('http://127.0.0.1:8000/gamestart', params, {headers})
        originImg.value=response.data.origin_img
        paintImg.value=response.data.paint_img
        answer.value=response.data.answer
        result.value=response.data.result

        store.commit('setOrigin',response.data.origin_img)
        store.commit('setPaint',response.data.paint_img)
        store.commit('setAnswer',response.data.answer)
        store.commit('setResult',response.data.result)
    })

    watch(img_timer.value, (newVal,oldVal) => {
        console.log(newVal,oldVal)
    })
</script>

<style scoped>
.hero {
  background: url('../assets/back.jpg');
  background-size: cover;
  height: 100vh;
}

.rotate{
    transform: rotate(270deg);
    border-radius: 12px;
    margin-top:150px;

}

.text{
    margin-left:300px;
    margin-right:300px;
}


</style>