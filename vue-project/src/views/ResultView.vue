<template>
  <v-app class="fill-height hero">
    <!-- 가로모드 화면 -->
    <v-container v-if="!isPortrait">
      <v-row class="justify-center">
        <!-- result logo 출력 -->
        <result :style="{ height: '15vh', margin: '0vh 0vw 5vh 0vw' }" />
      </v-row>

      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 5vh 0vw' }">
        <!-- 오디오 버튼 -->
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-if="audioInfo == true">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-if="audioInfo == false">
          </v-icon>
        </v-btn>
      </v-row>

      <v-row>
        <!-- 이미지를 3x3으로 출력 -->
        <v-col
          v-for="n in 9"
          :key="n"
          class="d-flex child-flex no-padding"
          cols="4"
        >
          <v-img
            :width="'45vw'"
            :height="'60vh'"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            cover
            :src="`data:image/gif;base64,${originImg[n - 1]}`"
            class="grey lighten-2"
            @click="moveDetail(n - 1)"
          >
          </v-img>
        </v-col>
      </v-row>

      <!-- 이미지 클릭시 나오는 dialog 정의 -->
      <v-dialog v-model="showDialog" max-height="75vh" max-width="100vw">
        <v-row>
          <!-- 이미지 label(정답) 출력 -->
          <v-col cols="4" class="mx-auto text-center nums">
            {{ answer[dialogNum] }}
          </v-col>
        </v-row>

        <v-row class="d-flex justify-center align-center">
          <!-- paint image 출력 -->
          <v-col cols="4" class="d-flex justify-center align-center">
            <v-img
              :src="`data:image/gif;base64,${paintImg[dialogNum]}`"
              max-height="50vh"
            />
          </v-col>
        </v-row>

        <v-row>
          <!-- dialog 닫는 버튼 -->
          <v-col cols="1" class="mx-auto">
            <v-btn color="primary" block @click="showDialog = false"
              >Close</v-btn
            >
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>

    <!-- 세로모드 -->
    <v-container v-if="isPortrait">
      <v-row class="justify-center">
        <!-- result logo 출력 -->
        <result :style="{ height: '10vh', margin: '3vh 0vw 10vh 0vw' }" />
      </v-row>

      <v-row>
        <!-- 이미지를 3x3으로 출력 -->
        <v-col
          v-for="n in 9"
          :key="n"
          class="d-flex child-flex no-padding"
          cols="4"
        >
          <v-img
            :width="'30vw'"
            :height="'20vh'"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            cover
            :src="`data:image/gif;base64,${originImg[n - 1]}`"
            class="grey lighten-2"
            @click="moveDetail(n - 1)"
          >
          </v-img>
        </v-col>
      </v-row>

      <!-- 이미지 클릭시 나오는 dialog 정의 -->
      <v-dialog v-model="showDialog" max-height="75vh" max-width="100vw">
        <v-row>
          <!-- 이미지 label(정답) 출력 -->
          <v-col cols="4" class="mx-auto text-center nums">
            {{ answer[dialogNum] }}
          </v-col>
        </v-row>

        <v-row class="d-flex justify-center align-center">
          <!-- paint image 출력 -->
          <v-col cols="9" class="d-flex justify-center align-center">
            <v-img
              :src="`data:image/gif;base64,${paintImg[dialogNum]}`"
              max-height="50vh"
            />
          </v-col>
        </v-row>

        <v-row>
          <!-- dialog 닫는 버튼 -->
          <v-col cols="3" class="mx-auto">
            <v-btn color="primary" block @click="showDialog = false"
              >Close</v-btn
            >
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>
  </v-app>
</template>

<script>
import result from "../svg/resultText.vue";
export default {
  components: {
    result,
  },
  data() {
    return {
      originImg: this.$store.state.originImg,
      paintImg: this.$store.state.paintImg,
      showDialog: false,
      dialogNum: false,
      answer: this.$store.state.answerList,
      audioInfo: true,
      isPortrait: true,
    };
  },
  methods: {
    checkOrientation() {
      this.isPortrait = window.screen.orientation.type === "portrait-primary";
    },
    moveDetail(index) {
      this.dialogNum = index;
      this.showDialog = true;
    },
    audioChange() {
      this.$root.audio.muted = !this.$root.audio.muted;
      this.audioInfo = !this.audioInfo;
    },
  },
  mounted() {
    this.checkOrientation();
    window.addEventListener("orientationchange", this.checkOrientation);
    this.$root.audio.play();
    this.audioInfo = !this.$root.audio.muted;
  },
  beforeUnmount() {
    window.removeEventListener("orientationchange", this.checkOrientation);
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
}

.no-padding {
  padding: 0;
}

@font-face {
  font-family: "answer";
  src: url("../fonts/Lobster-Regular.ttf");
}

.nums {
  font-family: "answer";
  font-size: 2.3rem;
  color: white;
}
</style>
