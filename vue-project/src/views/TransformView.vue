<template>
  <v-app class="hero fill-height">
    <!-- 가로 모드 -->
    <v-container v-if="isPortrait == false">
      <v-row>
        <v-col cols="3" />
        <!-- save paint 로고 출력 -->
        <v-col cols="6" class="d-flex justify-center">
          <logo :style="{ height: '15vh', margin: '7vh 0vw 0vh 0vw' }" />
        </v-col>

        <!-- 음향 버튼 -->
        <v-col cols="1" class="d-flex align-end">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!-- 홈 버튼 -->
        <v-col cols="1" class="d-flex align-end">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!--dialog 출력 버튼 -->
        <v-col cols="1" class="d-flex align-end">
          <v-btn rounded variant="plain" @click="showDialog = true" height="5vh">
            <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <!-- description dialog -->
      <v-dialog v-model="showDialog">
        <v-card>
          <!-- description text -->
          <v-card-title class="text-center" height="3vh">변환하려는 이미지를 업로드하면, 그림으로 다시
            그려드려요!</v-card-title>

          <!-- dialog close 버튼 -->
          <v-card-actions>
            <v-spacer />
            <v-btn variant="tonal" color="primary" @click="showDialog = false">확인</v-btn>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-row :style="{ margin: '2vh 0vw 0vh 0vw' }">
        <!-- 이전 이미지 출력 -->
        <v-col cols="5">
          <v-img src="../assets/tower-bridge.jpg" width="30vw" class="mx-auto" v-show="uploaded == false" />
          <v-img max-height="25vh" class="mx-auto" max-width="30vw" :src="imageUrl" v-show="uploaded == true" />
        </v-col>

        <!-- 화살표 -->
        <v-col cols="2" class="d-flex align-center justify-center">
          <v-icon icon="mdi-arrow-right-bold" size="5vh"> </v-icon>
        </v-col>

        <!-- 결과 이미지 출력 & 로딩 표시-->
        <v-col cols="5">
          <v-img src="../assets/tower-bridge-paint.jpg" width="30vw" class="mx-auto" v-show="uploaded == false" />
          <v-img max-height="25vh" class="mx-auto" max-width="30vw" :src="`data:image/gif;base64,${returnImg}`">
            <v-progress-circular v-if="transform == true" class="loading" color="grey-lighten-4"
              indeterminate></v-progress-circular>
          </v-img>
        </v-col>
      </v-row>

      <v-row :style="{ margin: '5vh 0vw 0vh 0vw' }">
        <!-- file upload block -->
        <v-col cols="6" class="mx-auto">
          <v-file-input clearable label="Upload your own image!" variant="solo" v-on:change="setImg"
            density="compact"></v-file-input>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center">
        <v-col cols="auto">
          <!-- transform 버튼 출력 -이미지 없으면 block -->
          <v-btn @click="transformImg" :disabled="image == null">Transform!</v-btn>
        </v-col>
      </v-row>


      <v-dialog v-model="alertDialog">
        <v-row class="d-flex justify-center">
          <v-col cols="6">
            <v-card>
              <v-card-title>
                Alert!
              </v-card-title>
              <v-card-text>
                지원하지 않는 파일 형식입니다!
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>

    <!-- 세로 모드 -->
    <v-container v-if="isPortrait == true">
      <v-row>
        <!-- save paint 로고 출력 -->
        <v-col cols="12" class="d-flex justify-center">
          <logo :style="{
            width: '90vw',
            height: '15vh',
            margin: '1vh 0vw 0vh 0vw',
          }" />
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center">
        <!-- 음향 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!-- 홈 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!--dialog 출력 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="showDialog = true" height="5vh">
            <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <!-- description dialog -->
      <v-dialog v-model="showDialog">
        <v-card>
          <!-- description text -->
          <v-card-title class="text-center" height="3vh">이미지를 밑 사진처럼 변합니다!</v-card-title>

          <!-- dialog close 버튼 -->
          <v-card-actions>
            <v-spacer />
            <v-btn variant="tonal" color="primary" @click="showDialog = false">확인</v-btn>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-row :style="{ margin: '2vh 0vw 0vh 0vw' }">
        <!-- file input block -->
        <v-col cols="12">
          <v-file-input clearable label="Upload your own image!" variant="solo" v-on:change="setImg"
            density="compact"></v-file-input>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center" :style="{ margin: '0vh 0vw 0vh 0vw' }">
        <!-- transform 버튼 -이미지 없으면 block -->
        <v-col cols="auto">
          <v-btn @click="transformImg" :disabled="image == null">Transform!</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <!-- default:예시 이미지 출력 -> 결과 이미지 출력 / 로딩표시 -->
        <v-col cols="12" class="d-flex justify-center" :style="{ margin: '2vh 0vw 0vh 0vw' }">
          <v-img src="../assets/tower-bridge-paint.jpg" width="100vw" v-show="uploaded == false" />
          <v-img max-width="100vw" class="mx-auto" :src="`data:image/gif;base64,${returnImg}`">
            <v-progress-circular v-if="transform == true" class="loading-mobile" color="grey-lighten-4"
              indeterminate></v-progress-circular>
          </v-img>
        </v-col>
      </v-row>


      <v-dialog v-model="alertDialog">
        <v-row class="d-flex justify-center">
          <v-col cols="12">
            <v-card>
              <v-card-title>
                Alert!
              </v-card-title>
              <v-card-text>
                지원하지 않는 파일 형식입니다!
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
export default {
  components: {
    logo,
  },
  /**
   * The data function for the component.
   *
   * @return {Object}
   *  The initial data for the component.
   *
   * @property {Byte} image - user upload image
   * @property {string} imageUrl - url made by image
   * @property {boolean} transform - The state of the transform for loading
   * @property {boolean} showDialog - The visibility state of the dialog.
   * @property {Byte} returnImg  - inferenced image of paint transformer from server
   * @property {boolean} uploaded - the state of user upload image for deleting default image
   * @property {boolean} audioInfo - The state of the audio (muted or not).
   * @property {boolean} isPortrait -  portrait mode or landscape mode
   */
  data() {
    return {
      image: null,
      transform: false,
      returnImg: null,
      uploaded: false,
      imageUrl: "",
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
      dialog: false,
      isPortrait: true,
      showDialog: false,
      alertDialog: false,
    };
  },
  /**
   * 디바이스가 가로모드인지 세로모드인지 확인하고 그에 맞는 event를 dom mount시 설정
   * @function mounted
   */
  mounted() {
    this.checkOrientation();
    window.addEventListener("orientationchange", this.checkOrientation);
    if (this.$root.audio.paused) {
      this.$root.audio.play();
    }
  },
  methods: {
    /**
     * 디바이스 가로 세로 모드 탐지 함수
     * @function checkOrientation
     */
    checkOrientation() {
      this.isPortrait = window.screen.orientation.type === "portrait-primary";
    },

    /**
     * image 업로드를 감지해 업로드된 이미지의 url을 생성하고 uploaded 변수를 true로 설정
     * @function setImg
     * @param {event} event
     */
    setImg(event) {
      this.image = event.target.files[0];
      this.uploaded = true;
      this.imageUrl = URL.createObjectURL(this.image);
    },

    /**
     * 유저가 업로드한 이미지를 formdata형태로 서버로 요청을 보내 inference data를 얻는 함수
     * @function transformImg
     */
    async transformImg() {
      // this.returnImg = null

      const formData = new FormData();
      formData.append("file", this.image);

      let availableExtension = ['image/jpg', 'image/png', 'image/jpeg']

      if (!availableExtension.includes(this.image.type)) {
        this.alertDialog = true
        return
      }
      this.transform = true;
      let response = await this.$api2(
        "http://34.64.169.197/api/v1/infer",
        "POST",
        formData
      );

      // let response = await this.$api2(
      //   "http://127.0.0.1:8000/api/v1/infer",
      //   "POST",
      //   formData
      // );
      this.returnImg = response;
      this.transform = false;

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
     * 홈버튼 클릭시 홈으로 이동
     * @function moveHome
     */
    moveHome() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<style>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.loading {
  margin-top: 10vh;
  margin-left: 10vw;
}

.loading-mobile {
  margin-top: 15vh;
  margin-left: 40vw;
}
</style>
