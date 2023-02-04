<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="d-flex justify-center">
        <!-- save paint! 로고 출력 -->
        <v-col cols="10" class="d-flex justify-center">
          <logo :style="{ height: '14vh', margin: '10vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>

      <!-- 모바일 ui(음향,홈,설명) -->
      <v-row class="d-flex d-sm-none justify-center">
        <!-- 음향(소리) 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="audioChange">
            <v-icon icon="mdi-volume-high" size="5vh" v-show="audioInfo == true">
            </v-icon>
            <v-icon icon="mdi-volume-off" size="5vh" v-show="audioInfo == false">
            </v-icon>
          </v-btn>
        </v-col>

        <!-- 홈 이동 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome">
            <v-icon icon="mdi-home-outline" size="5vh" />
          </v-btn>
        </v-col>

        <!-- 설명 dialog 버튼-->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="showDialog = true">
            <v-icon icon="mdi-information-outline" size="5vh" />
          </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="2" sm="4" />

        <!-- category logo 출력 -->
        <v-col cols="8" sm="4" class="d-flex justify-center align-center">
          <category :style="{ height: '6vh', width: '70vw', margin: '5vh 0vw 1vh 0vw' }" />
        </v-col>

        <v-col cols="2" sm="4">
          <!-- 음향(소리) 버튼 -->

          <v-row class="d-none d-sm-flex justify-end" :style="{ margin: '1vh 0vw 0vh 0vw', height: '5vh' }">
            <v-btn rounded variant="plain" @click="audioChange">
              <v-icon icon="mdi-volume-high" size="5vh" v-if="audioInfo == true">
              </v-icon>
              <v-icon icon="mdi-volume-off" size="5vh" v-if="audioInfo == false">
              </v-icon>
            </v-btn>
          </v-row>

          <!-- 홈 이동 버튼 -->

          <v-row class="d-none d-sm-flex justify-end" :style="{ margin: '1vh 0vw 0vh 0vw', height: '5vh' }">
            <v-btn rounded variant="plain" @click="moveHome">
              <v-icon icon="mdi-home-outline" size="5vh" />
            </v-btn>
          </v-row>

          <!-- 설명 dialog 버튼-->

          <v-row class="d-none d-sm-flex justify-end" :style="{ margin: '1vh 0vw 0vh 0vw', height: '5vh' }">
            <v-btn rounded variant="plain" @click="showDialog = true">
              <v-icon icon="mdi-information-outline" size="5vh" />
            </v-btn>
          </v-row>
        </v-col>
      </v-row>

      <!-- description dialog -->
      <v-dialog v-model="showDialog">
        <v-row class="justify-center">
          <v-col cols="12" sm="6">
            <v-card>
              <!-- dialog text -->
              <v-card-text class="text-center" height="3vh">
                카테고리에 해당하는 그림이 생성돼요. 그림을 보고 무엇인지 빨리
                맞혀보세요!
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <!-- dialog close 버튼 -->
                <v-btn variant="tonal" @click="showDialog = false" :style="{ margin: '0vh 0vw 0vh 30vw' }">확인</v-btn>

                <v-spacer></v-spacer>
                <!-- description 이동 버튼 -->
                <v-btn variant="tonal" @click="movePage('/description')" :style="{ margin: '0vh 30vw 0vh 0vw' }">게임방법
                  알아보기</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-dialog>

      <v-row class="d-flex justify-center">
        <!-- category 선택 버튼 - radio type -->
        <v-radio-group v-model="selectedCategory">
          <v-btn rounded v-for="item in categoryItems" :key="item.value" :value="item.value"
            @click="changeCategory(item.value)" :class="{
              selected: selectedCategory === item.value,
              ' mx-auto ': true,
            }" :style="{
  height: '4vh',
  width: '23vh',
  margin: '1.5vh 0vw 0vh 0vw',
}">
            {{ item.text }}
          </v-btn>
        </v-radio-group>
      </v-row>

      <!-- game 페이지 이동 버튼 -->
      <v-row>
        <v-col cols="12" class="d-flex justify-center" :style="{ margin: '3vh 0vw 0vh 0vw' }">
          <v-btn color="yellow" @click="startGame">Game start</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
import category from "../svg/categoryView.vue";

export default {
  components: {
    logo,
    category,
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
      categoryItems: [
        { text: "Animal", value: "animal" },
        { text: "Landmark", value: "landmark" },
        { text: "Celebrity", value: "entertainer" },
      ],
      selectedCategory: "animal",
      audioInfo: true,
      showDialog: false,
    };
  },

  methods: {
    /**
     * button event of routing to gameview and store category and mode to local storage
     * @function startGame
     */
    startGame() {
      this.$store.commit("setCategory", this.selectedCategory);
      this.$store.commit("setMode", this.selectedMode);
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
    audioChange() {
      this.$root.audio.muted = !this.$root.audio.muted;
      this.audioInfo = !this.audioInfo;
    },

    /**
     * 홈 버튼 클릭시 홈화면으로 이동하는 이벤트 함수
     * @function moveHome
     */
    moveHome() {
      this.$router.push({ path: "/" });
    },
  },
  mounted() {
    if (this.$root.audio.paused) {
      this.$root.audio.play();
    }
    this.audioInfo = !this.$root.audio.muted;
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.selected {
  background-color: rgb(248, 207, 71);
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
