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
                <v-img @load="imageLoaded = true" class="mx-auto" :src="gameStatusImage" height="350" width="350" v-show="game_status!=0"/>
            </v-col>
            <v-col cols=4>
            <v-progress-linear
                    v-show="game_status>0 && imageLoaded"
                    class="rotate"
                    height="20"
                    width="40"
                    v-model="total_timer">
            </v-progress-linear>
            </v-col>
        </v-row>
        <v-row class="d-flex justify-center mt-8">
            <v-col cols=4>
                <v-progress-linear v-show="game_status>0 && imageLoaded" v-model="img_timer" height="7" rounded color="indigo" ></v-progress-linear>
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

<script>
    import { ref } from 'vue'

/*
image_timer : 이미지 한장당 타이머 -> 퍼센트
total_timer : 모든 이미지에 대한 타이머 -> 퍼센트
text: 정답 text
test: 테스트용
head_text: 맨 위에 나올 text 게임 시작 전엔 save paint -> 문제 개수로 바뀜
game_status: 시작 전 0 각 문제 마다 +1(총 9) -> 게임이 끝날 때 10
*/
    export default{
        setup(){
            const img_timer=ref(100)
            const total_timer=ref(100)

            setInterval(() => {
                img_timer.value = img_timer.value - 1;
                total_timer.value = total_timer.value-1;
            }, 100);

            return{
                img_timer,
                total_timer
            }
        },
        data(){
            return {
                imageLoaded: false,
                text:'',
                test:0,
                head_text:'Save Paint!',
                game_status:0,
                originImg:[],
                paintImg:[],
                answer:[]
            };
        },
        computed: {
            gameStatusImage() {
                return 'data:image/gif;base64,'+this.paintImg[this.game_status-1]
            },
        },

        // created(){
        //     this.getGame()
        // },

        methods:{
            async getGame(){
               let response = await this.$api('http://127.0.0.1:8000/gamestart','POST',{category:this.$route.query.category,mode:this.$route.query.mode})
               this.originImg=response['origin_img']
               this.paintImg=response['paint_img']
               this.answer=response['answer']
               this.result=response['result']
                
               this.$store.commit('setOrigin',response['origin_img'])
               this.$store.commit('setPaint',response['paint_img'])
               this.$store.commit('setAnswer',response['answer'])
               this.$store.commit('setResult',response['result'])
               
            },
            
            enter(){
                if (this.text===this.answer[this.game_status-1]){
                    this.text=''
                    this.game_status+=1
                }
                if (this.game_status===10){
                    this.$router.push({path: '/result',props:{originImg:this.originImg,paintImg:this.paintImg,answer:this.answer}})
                }

            },

            startGame(){
                this.game_status+=1
                this.getGame()
                this.img_timer.value=100
                this.total_timer.value=100
            },
            
        }
    }


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