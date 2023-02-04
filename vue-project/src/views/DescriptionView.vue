<template>
  <v-app class="hero">
    <!-- 가로 모드 -->
    <v-overlay v-model="overlay" width="100%" height="100%" persistent>
      <v-container v-if="!isPortrait">
        <v-row class="justify-center">
          <v-col cols="1"></v-col>
          <v-col cols="8" class="d-flex justify-center">
            <!-- 문제 번호 / 문제 수 출력-->
            <div
              class="round"
              :style="{
                color: page === 2 ? 'white' : 'grey',
              }"
            >
              2/9
            </div>
          </v-col>

          <v-col cols="1">
            <!-- 오디오 버튼 -->
            <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
              <v-icon :icon="audioIcon" size="5vh" color="white"> </v-icon>
            </v-btn>
            <br />
            <!-- 뒤로가기 버튼 -->
            <v-btn
              rounded
              variant="plain"
              @click="moveBack"
              :style="{ height: '5vh', 'margin-top': '5vh' }"
            >
              <back height="5vh" />
            </v-btn>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="4"></v-col>
          <v-col cols="4">
            <!-- GIF/이미지를 출력 -->
            <v-img
              :src="getImageSrc"
              class="mx-auto"
              height="35vh"
              width="40vw"
            />
          </v-col>
          <v-col cols="4" class="mx-auto">
            <!-- 전체 타이머에 대한 프로그래스 바 -->
            <v-progress-linear
              :class="getBarClass"
              height="20vh"
              v-model="totalTimer"
            />
          </v-col>
        </v-row>
        <v-row class="d-flex justify-center text-center">
          <v-col>
            <!-- 하나의 이미지에 대한 타이머 프로그래스 바 / 시간 초 출력 5초 이하로 남을 시 빨간색으로 표시-->
            <v-progress-circular
              :color="getCircleColor"
              height="4vh"
              :size="65"
              :width="8"
              model-value="100"
            >
              <div
                :style="{
                  'font-size': '3vh',
                  color: 'black',
                }"
              >
                {{ 12 }}
              </div>
            </v-progress-circular>
          </v-col>
        </v-row>
        <v-row class="d-flex justify-center" :style="{ 'margin-top': '1vh' }">
          <!-- 정답 글자 수 표시 -->
          <div :style="{ display: 'flex' }">
            <v-sheet
              v-for="i in 3"
              :key="i"
              :color="getSheetColor"
              elevation="1"
              height="6vh"
              width="6vh"
              rounded
              :style="{ 'margin-left': '2vw' }"
            />
          </div>
        </v-row>
        <v-row>
          <v-col cols="4"></v-col>
          <v-col cols="4" class="d-flex justify-center">
            <!-- 정답 입력 칸 -->
            <v-text-field
              readonly
              label="Enter the answer"
              single-line
              density="compact"
              :bg-color="getTextFieldBgColor"
            />
          </v-col>
        </v-row>
        <!-- 각각의 화면 구성 요소에 대한 설명 글 -->
        <div class="explanation text-center">
          {{ getExplanation }}
          <br />
          <v-btn
            v-if="page >= 2"
            class="ma-2"
            icon="mdi-arrow-left-bold"
            variant="text"
            @click="changeQuery(this.page - 1)"
          />
          <v-btn
            v-if="page < 7"
            icon="mdi-arrow-right-bold"
            variant="text"
            @click="changeQuery(this.page + 1)"
          />
        </div>
      </v-container>
      <!-- 세로 모드 -->
      <v-container v-if="isPortrait">
        <v-row class="justify-center">
          <v-col cols="1"></v-col>
          <v-col cols="8" class="d-flex justify-center">
            <!-- 문제 번호 / 문제 수 출력-->
            <div
              class="mobile-round"
              :style="{
                color: page === 2 ? 'white' : 'grey',
              }"
            >
              2/9
            </div>
          </v-col>
          <v-col cols="1">
            <div class="d-flex align-center">
              <!-- 오디오 버튼 -->
              <v-btn rounded variant="plain" @click="changeAudio" height="3vh">
                <v-icon :icon="audioIcon" size="3vh" color="white"> </v-icon>
              </v-btn>
            </div>
            <br />
            <!-- 뒤로가기 버튼 -->
            <div class="d-flex align-center">
              <v-btn rounded variant="plain" @click="moveBack" height="3vh">
                <back height="3vh" />
              </v-btn>
            </div>
          </v-col>
        </v-row>
        <v-row :style="{ 'margin-top': '5vw', 'margin-bottom': '5vw' }">
          <v-col cols="12" class="mx-auto">
            <!-- 전체 타이머에 대한 프로그래스 바 -->
            <v-progress-linear
              height="7vw"
              :class="getMobileBarClass"
              v-model="totalTimer"
            />
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12">
            <!-- GIF/이미지를 출력 -->
            <v-img
              :src="getImageSrc"
              class="mx-auto"
              height="30vh"
              width="70vw"
            />
          </v-col>
        </v-row>

        <v-row class="d-flex justify-center text-center">
          <v-col>
            <!-- 하나의 이미지에 대한 타이머 프로그래스 바 / 시간 초 출력 5초 이하로 남을 시 빨간색으로 표시-->
            <v-progress-circular
              :color="getCircleColor"
              height="2.5vh"
              :size="65"
              :width="8"
              model-value="100"
            >
              <div
                :style="{
                  'font-size': '1.5vh',
                  color: 'black',
                }"
              >
                {{ 12 }}
              </div>
            </v-progress-circular>
          </v-col>
        </v-row>

        <v-row class="d-flex justify-center" :style="{ 'margin-top': '1vh' }">
          <!-- 정답 글자 수 표시 -->
          <div :style="{ display: 'flex' }">
            <v-sheet
              v-for="i in 3"
              :key="i"
              :color="getSheetColor"
              elevation="1"
              height="4vh"
              width="4vh"
              rounded
              :style="{ 'margin-left': '2vw' }"
            />
          </div>
        </v-row>

        <v-row :style="{ 'margin-top': '5vw', 'margin-bottom': '5vw' }">
          <!-- 정답 입력 칸 -->
          <v-text-field
            readonly
            label="Enter the answer"
            single-line
            density="compact"
            :bg-color="getTextFieldBgColor"
          />
        </v-row>
        <!-- 각각의 화면 구성 요소에 대한 설명 글 -->
        <div class="mobile-explanation text-center">
          {{ getExplanation }}
          <br />
          <v-btn
            v-if="page >= 2"
            class="ma-2"
            icon="mdi-arrow-left-bold"
            variant="text"
            @click="changeQuery(this.page - 1)"
          />
          <v-btn
            v-if="page < 7"
            icon="mdi-arrow-right-bold"
            variant="text"
            @click="changeQuery(this.page + 1)"
          />
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
  /**
   * The data function for the component.
   *
   * @return {Object}
   *  The initial data for the component.
   *

   * @property {boolean} audioIcon - The state of the audio (muted or not).
   * @property {boolean} overlay - overlay for explanation
   * @property {boolean} totalTimer - time left
   * @property {boolean} page - current page
   * @property {boolean} isPortrait -  portrait mode or landscape mode
   */
  data() {
    return {
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
      overlay: false,
      totalTimer: 25,
      page: 1,
      isPortrait: true,
    };
  },

  computed: {
    getImageSrc() {
      return this.page === 3
        ? require("@/assets/bird.gif")
        : require("@/assets/bird_overlayed.jpg");
    },
    getBarClass() {
      return this.page === 7 ? "bar" : "overlayed-bar";
    },
    getMobileBarClass() {
      return this.page === 7 ? "mobile-bar" : "overlayed-mobile-bar";
    },
    getCircleColor() {
      return this.page === 4 ? "#0000FF" : "#1E3269";
    },
    getSheetColor() {
      return this.page === 5 ? "white" : "grey";
    },
    getTextFieldBgColor() {
      return this.page === 6 ? "white" : null;
    },
    getExplanation() {
      switch (this.page) {
        case 1:
          return "게임 화면의 구성을 설명할게요.";
        case 2:
          return "1.현재 진행중인 게임 라운드예요.";
        case 3:
          return "2.현재 라운드에 해당하는 이미지가 생성돼요.";
        case 4:
          return "3. 현재 라운드의 남은 시간이에요. 제한시간 내에 정답을 맞히지 못하면 다음 이미지로 넘어가요!";
        case 5:
          return " 4. 정답이 몇 글자인지 알려줘요.";
        case 6:
          return "5. 정답을 입력할 수 있는 칸이에요.";
        case 7:
          return "6. 남은 물감의 총량이에요. 그림을 그리면서 물감이 소모되고, 소진 시 미션 실패로 게임이 종료돼요.";
        default:
          return "";
      }
    },
  },
  /**
   * 디바이스가 가로모드인지 세로모드인지 확인하고 그에 맞는 event를 dom mount시 설정
   * @function mounted
   */
  mounted() {
    this.overlay = true;
    this.checkOrientation();
    window.addEventListener("orientationchange", this.checkOrientation);
  },
  beforeUnmount() {
    window.removeEventListener("orientationchange", this.checkOrientation);
  },
  methods: {
    /**
     * 원하는 페이지로 이동하는 함수
     * @function changeQuery
     * @param {next} next
     */
    changeQuery(next) {
      this.page = next;
    },
    /**
     * 이전 페이지인 select로 이동하는 함수
     * @function moveBack
     */
    moveBack() {
      this.$router.push({ path: "/select" });
    },
    /**
     * 오디오 버튼 클릭으로 오디오를 끄거나 키는 이벤트 함수
     * @function changeAudio
     */
    changeAudio() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioIcon =
        this.audioIcon === "mdi-volume-high"
          ? "mdi-volume-off"
          : "mdi-volume-high";
    },
    /**
     * 디바이스 가로 세로 모드 탐지 함수
     * @function checkOrientation
     */
    checkOrientation() {
      this.isPortrait = window.screen.orientation.type === "portrait-primary";
    },
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

.overlayed-bar {
  color: grey;
  transform: rotate(90deg);

  margin-top: 20vh;
  background: linear-gradient(
    to right,
    #e5404023 0%,
    #ffa63a23 16%,
    #dcff3f38 32%,
    #6cff3f46 48%,
    #3fa2ff3b 64%,
    #a53fff38 80%,
    #ff3fc93b 100%
  );

  border-radius: 30px;
}

.bar {
  color: white;
  transform: rotate(90deg);
  margin-top: 20vh;
  background: linear-gradient(
    to right,
    #e54040 0%,
    #ffa63a 16%,
    #dcff3f 32%,
    #6cff3f 48%,
    #3fa2ff 64%,
    #a53fff 80%,
    #ff3fc9 100%
  );
  border-radius: 30px;
}

.overlayed-mobile-bar {
  color: grey;
  transform: rotate(180deg);
  background: linear-gradient(
    to right,
    #e5404023 0%,
    #ffa63a23 16%,
    #dcff3f38 32%,
    #6cff3f46 48%,
    #3fa2ff3b 64%,
    #a53fff38 80%,
    #ff3fc93b 100%
  );

  border-radius: 30px;
}

.mobile-bar {
  color: white;
  transform: rotate(180deg);
  background: linear-gradient(
    to right,
    #e54040 0%,
    #ffa63a 16%,
    #dcff3f 32%,
    #6cff3f 48%,
    #3fa2ff 64%,
    #a53fff 80%,
    #ff3fc9 100%
  );
  border-radius: 30px;
}

.round {
  font-size: 5vw;
  height: 11vh;
  font-family: "num";
}

.mobile-round {
  font-size: 10vw;
  height: 12vh;
  font-family: "num";
}

.explanation {
  font-size: 3vh;
  color: white;
}

.mobile-explanation {
  font-size: 2vh;
  color: white;
}
</style>
