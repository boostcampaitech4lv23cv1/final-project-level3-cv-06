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
        <v-col cols="1" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <v-col cols="1" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <v-col cols="1" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveRank" height="5vh">
            <v-icon icon="mdi-refresh" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <!-- 이미지를 3x3으로 출력 -->
        <v-col v-for="n in 9" :key="n" class="d-flex child-flex no-padding" cols="4">
          <v-img :width="'45vw'" :height="'60vh'" :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1" cover :src="`${originImg[n - 1]}`" class="grey lighten-2" @click="moveDetail(n - 1)">
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
            <v-img :src="`${paintImg[dialogNum]}`" max-height="50vh" />
          </v-col>
        </v-row>

        <v-row>
          <!-- dialog 닫는 버튼 -->
          <v-col cols="1" class="mx-auto">
            <v-btn color="primary" block @click="showDialog = false">Close</v-btn>
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>

    <!-- 세로모드 -->
    <v-container v-if="isPortrait">
      <v-row class="justify-center">
        <!-- result logo 출력 -->
        <result :style="{ height: '10vh', margin: '3vh 0vw 0vh 0vw' }" />
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 5vh 0vw' }">
        <!-- 오디오 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveRank" height="5vh">
            <v-icon icon="mdi-refresh" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <!-- 이미지를 3x3으로 출력 -->
        <v-col v-for="n in 9" :key="n" class="d-flex child-flex no-padding" cols="4">
          <v-img :width="'30vw'" :height="'20vh'" :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1" cover :src="`${originImg[n - 1]}`" class="grey lighten-2" @click="moveDetail(n - 1)">
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
            <v-img :src="`${paintImg[dialogNum]}`" max-height="50vh" />
          </v-col>
        </v-row>

        <v-row>
          <!-- dialog 닫는 버튼 -->
          <v-col cols="3" class="mx-auto">
            <v-btn color="primary" block @click="showDialog = false">Close</v-btn>
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
  /**
   * The data function for the component.
   *
   * @return {Object}
   *  The initial data for the component.
   *
   * @property {Array<String>} originImg 원본 이미지의 url을 갖고있는 배열
   * @property {Array<String>} paintImg 게임 이미지의 url을 갖고있는 배열
   * @property {Boolean} showDialog originImg 클릭시 paintImg를 보여주기위한 dialog를 열고 닫기 위한 변수
   * @property {Number} dialogNum 몇번째 사진을 클릭했는지 확인하기 위한 변수
   * @property {Array<String>} answer 각 사진들의 answer label을 출력하기 위한 배열
   * @property {Boolean} audioinfo 오디오 on off 를 위한 변수
   * @property {Boolean} isPortrait device의 가로모드 세로모드를 구별하기 위한 변수
   */
  data() {
    return {
      originImg: this.$store.state.originImg,
      paintImg: this.$store.state.paintImg,
      showDialog: false,
      dialogNum: 0,
      answer: this.$store.state.answerList,
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
      isPortrait: true,
    };
  },

  methods: {
    /**
     * device의 가로 세로 모드를 구별하기 위한 함수
     * @function checkOrientation
     */
    checkOrientation() {
      this.isPortrait = window.screen.orientation.type === "portrait-primary";
    },

    /**
     * 이미지 클릭시 gif dialog를 보여주기 위해 이미지 index를 설정하는 이벤트 함수
     * @function moveDetail
     */
    moveDetail(index) {
      this.dialogNum = index;
      this.showDialog = true;
    },

    /**
     * 오디오 버튼 클릭시 on off를 하기 위한 이벤트 함수
     * @function audioChange
     */
    changeAudio() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
        this.audioIcon = "mdi-volume-high";
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
        this.audioIcon =
          this.audioIcon === "mdi-volume-high"
            ? "mdi-volume-off"
            : "mdi-volume-high";
      }
    },
    moveHome() {
      this.$router.push({ path: "/" });
    },
    moveRank() {
      this.$router.push({ path: "/rank" })
    }
  },

  /**
   * 페이지 생성시 가로 세로 모드를 구별하고 오디오 자동 재생을 하기 위한 함수
   * @function mounted
   */
  mounted() {
    this.checkOrientation();
    window.addEventListener("orientationchange", this.checkOrientation);
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
