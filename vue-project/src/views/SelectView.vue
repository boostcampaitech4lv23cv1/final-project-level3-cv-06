<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-alert class="d-flex d-sm-none justify-center" v-if="isIOS" density="compact" type="info"
        title="아이폰은 지원되지 않아요.">
      </v-alert>
      <v-row class="d-flex justify-center">
        <!-- save paint! 로고 출력 -->
        <v-col cols="10" class="d-flex justify-center">
          <logo :style="{ height: '14vh', margin: '10vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>


      <!-- 모바일 ui(음향,홈,설명) -->
      <v-row class="d-flex justify-center">
        <!-- 음향(소리) 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
          <br />
        </v-col>


        <!-- 홈 이동 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh" />
          </v-btn>
        </v-col>


        <!-- 설명 dialog 버튼-->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="showDialog = true" height="5vh">
            <v-icon icon="mdi-information-outline" size="5vh" />
          </v-btn>
        </v-col>
      </v-row>


      <!-- description dialog -->
      <v-dialog v-model="showDialog">
        <v-row class="justify-center">
          <v-col cols="12" sm="6">
            <v-card>
              <!-- dialog text -->
              <v-card-text class="text-center" height="10vh">
                카테고리에 해당하는 그림이 생성돼요. 그림을 보고
                무엇인지 빨리 맞혀보세요!
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <!-- dialog close 버튼 -->
                <v-btn variant="tonal" @click="showDialog = false" :style="{ margin: '0vh 0vw 0vh 0vw' }"
                  color="#6fc2fe">확인</v-btn>
                <v-spacer></v-spacer>
                <!-- description 이동 버튼 -->
                <v-btn variant="tonal" @click="movePage('/description')" :style="{ margin: '0vh 0vw 0vh 0vw' }"
                  color="#6fc2fe">게임방법 알아보기</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-dialog>
      <v-row class="text-center text-h6 text-black font-weight-bold" :style="{ 'margin-top': '5vh' }">
        <v-col cols="3"> 인물 </v-col>
        <v-col cols="3"> 동물 </v-col>
        <v-col cols="3"> 포켓몬 </v-col>
        <v-col cols="3"> 나라 </v-col>
      </v-row>
      <v-row justify="center">
        <template v-for="(item, i) in items" :key="i">
          <v-col cols="3">
            <v-hover v-slot="{ isHovering, props }">
              <v-card class="mx-auto" @click="[changeCategory(item.value), startGame()]"
                :elevation="isHovering ? 12 : 2" :class="{ 'on-hover': isHovering }" v-bind="props">
                <v-img :src="item.img" cover height="25vh"> </v-img>
              </v-card>
            </v-hover>
          </v-col>
        </template>

      </v-row>
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
   * @property {Array<{text: string, value: string}>} categoryItems - The list of category items.
   * @property {string} selectedCategory - The selected category.
   * @property {boolean} audioInfo - The state of the audio (muted or not).
   * @property {boolean} showDialog - The visibility state of the dialog.
   */
  data() {
    return {
      items: [
        {
          title: "인물",
          value: "celebrity",
          img: require("../assets/IU.jpg"),
        },
        {
          title: "동물",
          value: "animal",
          img: require("../assets/animal.jpg"),
        },
        {
          title: "포켓몬",
          value: "pokemon",
          img: require("../assets/pikachu.jpg"),
        },
        {
          title: "나라",
          value: "landmark",
          img: require("../assets/eiffel.jpg"),
        },
      ],
      transparent: "rgba(255, 255, 255, 0)",
      selectedCategory: "",
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
      showDialog: false,
      isIOS: false,
    };
  },
  created() {
    this.isIOS =
      /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  },
  methods: {
    /**
     * button event of routing to gameview and store category and mode to local storage
     * @function startGame
     */
    startGame() {
      this.$store.commit("setCategory", this.selectedCategory);
      this.$router.push({
        path: "/game",
      });
    },

    /**
     * 버튼 클릭시 지정된 페이지로 이동하는 이벤트 함수
     * @function movePage
     * @param {string} route  이동할 페이지
     */
    movePage(route) {
      this.$router.push({
        path: route,
      });
    },

    /**
     * 버튼 클릭시 클릭한 버튼의 value로 카테고리 값을 바꾸어 주는 이벤트 함수
     * @function changeCategory
     * @param {string} value
     */
    changeCategory(value) {
      this.selectedCategory = value;
    },

    /**
     * 오디오 버튼 클릭으로 오디오를 끄거나 키는 이벤트 함수
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
    /**
     * 홈 버튼 클릭시 홈화면으로 이동하는 이벤트 함수
     * @function moveHome
     */
    moveHome() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.v-card {
  transition: opacity 0.4s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.8;
}

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}

@media only screen and (max-width: 480px) {
  .icon-size {
    width: 2vh;
    height: 2vh;
  }
}

@media only screen and (min-width: 480px) {
  .icon-size {
    width: 5vh;
    height: 5vh;
  }
}
</style>
