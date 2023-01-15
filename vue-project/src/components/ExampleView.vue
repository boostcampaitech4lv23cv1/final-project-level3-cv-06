<template>

    <v-overlay v-model="overlay" z-index="500" width="100%" height="100%">
    
        <v-container @click.stop style="position: relative">
            <v-row>
                <v-col cols=12></v-col>
                <v-col cols=12></v-col>
            </v-row>
            <v-row class="justify-center">
                <v-col cols="4" class="d-flex justify-center align-center text-white no-overlay-container">
                    <div v-show="page==1">
                    1.현재 진행중인 게임 라운드와 총 라운드 수입니다.
                    <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="moveHome"/>
                    <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(2)"/>
                    </div>
                </v-col>
                <div :style="{ 'font-size': '30px', 'color': 'white' }"  class="no-overlay-container">4/9</div>
                <v-col cols="2"></v-col>
                <v-col cols="2" class="justify-center align-center text-white no-overlay-container">
                    <div v-show="page==4">
                    4. 남은 물감의 양입니다. 그림을 그리면서 물감이 소모되며, 소진 시 미션 실패로 게임이 종료됩니다
                    <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(3)"/>
                    <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="moveHome"/>
                    </div>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols=12></v-col>
            </v-row>
            <v-row>
                <v-col cols="4" class="d-flex justify-center align-center text-white no-overlay-container" style="position: relative; top: 100px;">
                    <div v-show="page==2">
                    2. 현재 라운드에 해당하는 이미지를 생성합니다.
                    <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(1)"/>
                    <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(3)"/>
                    </div>
                </v-col>
                <v-img src="../assets/example.jpg" height="270" width="270" class="no-overlay-container" />
                <v-col></v-col>
                <v-col cols="3" class='rotate'>
                        <v-progress-linear
                            height="20"
                            width="40"
                            v-model="valueDeterminate"
                            >
                        </v-progress-linear>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols=12 ><v-spacer></v-spacer></v-col>
                <v-col cols=12  class="d-flex justify-center align-center text-white no-overlay-container">
                <div v-show="page==3">
                3. 정답을 입력할 수 있는 칸입니다.
                <br/>
                <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(2)"/>
                <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(4)"/>
                </div>
                </v-col>
            </v-row>

            <v-row  class="justify-center">
                <v-col cols="4">
                    <v-text-field
                        clearable
                        hide-details="auto"
                        label="Answer"
                        ></v-text-field>
                </v-col>
            </v-row>
        </v-container> 
    </v-overlay>
</template>



<script>

    export default {
        props:['page'],
        data(){
                return {
                    valueDeterminate: 50,
                    overlay: true,
                };
            },
        methods:{
            changeQuery(next) {
                this.$router.replace({ query: { page: next } })
                },
            moveHome(){
                this.$router.push({path:'/'})
            }
        }
    }

</script>


<style scoped>
.no-overlay-container {
  position: relative;
  z-index: 1000;
}
.v-progress-linear{
  border-radius: 12px;
}

.rotate{
    transform: rotate(270deg)
}

</style>