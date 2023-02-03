<template>
  <v-app class="hero">
    <v-overlay v-model="overlay" width="100%" height="100%" :style="{ backgroundColor: '#999999' }">
      <v-container>
        <v-row class="d-flex justify-center nums">
          <div v-if="page == 2" :style="{
            'font-size': '5vw',
            color: 'white',
          }" class="text-center">
            2/9
          </div>
          <div v-else :style="{
            'font-size': '5vw',
            color: 'black',
          }" class="text-center">
            2/9
          </div>
        </v-row>
        <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
          <v-btn rounded variant="plain" @click="audioChange" height="5vh">
            <v-icon icon="mdi-volume-high" size="5vh" v-show="audioInfo == true" color="white">
            </v-icon>
            <v-icon icon="mdi-volume-off" size="5vh" v-show="audioInfo == false" color="white">
            </v-icon>
          </v-btn>
        </v-row>

        <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
          <v-btn rounded variant="plain" @click="moveBack" height="5vh">
            <back height="5vh" />
          </v-btn>
        </v-row>

        <v-row class="d-flex">
          <v-col cols="4"></v-col>
          <v-col cols="4">
            <v-img v-if="page == 3" class="mx-auto" src="../assets/bird.gif" height="25vh" width="25vw" />
            <v-img v-if="page != 3" class="mx-auto" src="../assets/bird_overlayed.jpg" height="25vh" width="25vw" />
          </v-col>
          <v-col cols="4" class="mx-auto">
            <v-progress-linear v-if="page == 7" class="bar" height="20vh" color="white" v-model="totalTimer">
            </v-progress-linear>
            <v-progress-linear v-if="page != 7" class="overlayedbar" height="20vh" color="grey" v-model="totalTimer">
            </v-progress-linear>
          </v-col>
        </v-row>
        <v-row class="d-flex justify-center text-center">
          <v-col>
            <v-progress-circular v-if="page == 4" height="5vh" color="#0000FF" :size="65" :width="8" model-value="100">
              <div :style="{
                'font-size': '3vh',
                color: 'black',
              }">
                {{ 12 }}
              </div>
            </v-progress-circular>

            <v-progress-circular v-if="page != 4" height="5vh" color="#1E3269" :size="65" :width="8" model-value="100">
              <div :style="{
                'font-size': '3vh',
                color: 'black',
              }">
                {{ 12 }}
              </div>
            </v-progress-circular>
          </v-col>
        </v-row>

        <v-row class="d-flex justify-center" :style="{ 'margin-top': '3vh' }">
          <div v-if="page == 5" style="display: flex">
            <v-sheet v-for="i in 3" :key="{ i }" color="white" elevation="1" height="7vh" width="6vh" rounded
              :style="{ 'margin-left': '1vw' }"></v-sheet>
          </div>
          <div v-if="page != 5" style="display: flex">
            <v-sheet v-for="i in 3" :key="{ i }" color="grey" elevation="1" height="7vh" width="6vh" rounded
              :style="{ 'margin-left': '1vw' }"></v-sheet>
          </div>
        </v-row>

        <v-row class="justify-center" :style="{ 'margin-top': '7vh', 'font-size': '1vh' }">
          <v-col cols="4">
            <v-text-field v-if="page == 6" readonly bg-color="white" label="answer" single-line
              density="compact"></v-text-field>
            <v-text-field v-if="page != 6" readonly label="answer" single-line density="compact"></v-text-field>
          </v-col>
        </v-row>
        <div v-if="page == 1" :style="{ 'font-size': '2vh', color: 'white' }" class="text-center">
          게임 화면의 구성을 설명할게요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(2)" />
        </div>
        <div v-if="page == 2" :style="{ 'font-size': '2vh', color: 'white', position: '' }" class="text-center">
          1.현재 진행중인 게임 라운드예요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(1)" />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(3)" />
        </div>
        <div v-if="page == 3" :style="{ 'font-size': '2vh', color: 'white', position: '' }" class="text-center">
          2.현재 라운드에 해당하는 이미지가 생성돼요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(2)" />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(4)" />
        </div>
        <div v-if="page == 4" :style="{ 'font-size': '2vh', color: 'white' }" class="text-center">
          3. 현재 라운드의 남은 시간이에요.<br />제한시간 내에 정답을 맞히지
          못하면<br />다음 이미지로 넘어가요!<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(3)" />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(5)" />
        </div>
        <div v-if="page == 5" :style="{ 'font-size': '2vh', color: 'white' }" class="text-center">
          4. 정답이 몇 글자인지 알려줘요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(4)" />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(6)" />
        </div>
        <div v-if="page == 6" :style="{ 'font-size': '2vh', color: 'white' }" class="text-center">
          5. 정답을 입력할 수 있는 칸이에요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(5)" />
          <v-btn class="ma-2" icon="mdi-arrow-right-bold" variant="text" @click="changeQuery(7)" />
        </div>

        <div v-if="page == 7" :style="{ 'font-size': '2vh', color: 'white' }" class="text-center">
          6. 남은 물감의 총량이에요.<br />
          그림을 그리면서 물감이 소모되고,<br />
          소진 시 미션 실패로 게임이 종료돼요.<br />
          <v-btn class="ma-2" icon="mdi-arrow-left-bold" variant="text" @click="changeQuery(6)" />
        </div>
      </v-container>
    </v-overlay>
  </v-app>
</template>
<script>
import back from "../svg/backButtonWhite.vue";
export default {
  components: {
    back,
  },
  data() {
    return {
      audioInfo: !this.$root.audio.muted,
      overlay: false,
      totalTimer: 25,
      page: 1
    };
  },

  mounted() {
    this.overlay = true;
  },
  methods: {
    changeQuery(next) {
      this.page += 1
    },
    moveBack() {
      this.$router.push({ path: "/select" });
    },
    audioChange() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioInfo = !this.audioInfo;
    }
  },
};
</script>
<style scoped>
.hero {
  background: url("../assets/canvas.jpg");
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
}

.overlayedbar {
  transform: rotate(90deg);

  margin-top: 20vh;
  background: linear-gradient(to right,
      #e5404023 0%,
      #ffa63a23 16%,
      #dcff3f38 32%,
      #6cff3f46 48%,
      #3fa2ff3b 64%,
      #a53fff38 80%,
      #ff3fc93b 100%);

  border-radius: 30px;
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

.nums {
  font-family: "num";
  font-size: 4rem;
}
</style>
