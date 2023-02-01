<template>
  <v-app class="hero">
    <v-overlay v-model="overlay" width="100%" height="100%" persistent>
      <v-overlay v-model="overlay" width="100%" height="100%" persistent>
        <v-overlay v-model="overlay" width="100%" height="100%" persistent>
          <v-container
            class="fill-height fill-width"
            @click.stop
            :style="{ position: 'relative' }"
          >
            <v-row class="d-flex justify-center nums">
              <div
                v-if="page == 2"
                :style="{
                  'font-size': '7vh',
                  color: 'white',
                }"
                class="text-center"
              >
                2/9
              </div>
              <div
                v-else
                :style="{
                  'font-size': '7vh',
                  color: 'black',
                }"
                class="text-center"
              >
                2/9
              </div>
            </v-row>
            <v-row
              class="d-flex justify-end"
              :style="{ margin: '3vh 0vw 0vh 0vw' }"
            >
              <v-btn rounded variant="plain" @click="audioChange" height="5vh">
                <v-icon
                  icon="mdi-volume-high"
                  size="5vh"
                  v-show="audioInfo == true"
                  color="white"
                >
                </v-icon>
                <v-icon
                  icon="mdi-volume-off"
                  size="5vh"
                  v-show="audioInfo == false"
                  color="white"
                >
                </v-icon>
              </v-btn>
            </v-row>

            <v-row
              class="d-flex justify-end"
              :style="{ margin: '3vh 0vw 0vh 0vw' }"
            >
              <v-btn rounded variant="plain" @click="moveHome">
                <v-icon icon="mdi-home-outline" size="5vh" color="white">
                </v-icon>
              </v-btn>
            </v-row>

            <v-row class="d-flex">
              <v-col cols="4"></v-col>
              <v-col cols="4">
                <v-img
                  v-if="page == 3"
                  class="mx-auto"
                  src="../assets/bird.gif"
                  height="40vh"
                  width="40vw"
                />
                <v-img
                  v-if="page != 3"
                  class="mx-auto"
                  src="../assets/bird_overlayed.jpg"
                  height="40vh"
                  width="40vw"
                />
              </v-col>
              <v-col cols="4" class="mx-auto">
                <div v-if="page == 6">
                  <v-progress-linear
                    class="bar"
                    height="20vh"
                    color="white"
                    v-model="totalTimer"
                  >
                  </v-progress-linear>
                </div>

                <div v-if="page != 6">
                  <v-progress-linear
                    class="overlayedbar"
                    height="20vh"
                    color="grey"
                    v-model="totalTimer"
                  >
                  </v-progress-linear>
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col cols="4">
                <div v-if="page == 4">
                  <v-img
                    class="mx-auto"
                    src="../assets/img_timer.jpg"
                    width="25vw"
                  />
                </div>
                <div v-else class="mx-auto">
                  <v-img
                    class="mx-auto"
                    src="../assets/img_timer_overlayed.jpg"
                    width="25vw"
                  />
                </div>
              </v-col>
              <v-spacer></v-spacer>
            </v-row>

            <v-row
              class="justify-center"
              :style="{ 'margin-top': '7vh', 'font-size': '1vh' }"
            >
              <v-col cols="4">
                <v-text-field
                  v-if="page == 5"
                  readonly
                  bg-color="white"
                  label="answer"
                  single-line
                  density="compact"
                ></v-text-field>
                <v-text-field
                  v-if="page != 5"
                  readonly
                  label="answer"
                  single-line
                  density="compact"
                ></v-text-field>
              </v-col>
            </v-row>
            <div
              v-if="page == 1"
              :style="{ 'font-size': '3vh', color: 'white' }"
              class="text-center"
            >
              게임 화면의 구성을 설명합니다.<br />
              <!-- <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="moveHome"
              /> -->
              <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="changeQuery(2)"
              />
            </div>
            <div
              v-if="page == 2"
              :style="{ 'font-size': '3vh', color: 'white', position: '' }"
              class="text-center"
            >
              1.현재 진행중인 게임 라운드입니다.<br />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="changeQuery(1)"
              />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="changeQuery(3)"
              />
            </div>
            <div
              v-if="page == 3"
              :style="{ 'font-size': '3vh', color: 'white', position: '' }"
              class="text-center"
            >
              2.현재 라운드에 해당하는 이미지를 생성합니다.<br />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="changeQuery(2)"
              />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="changeQuery(4)"
              />
            </div>
            <div
              v-if="page == 4"
              :style="{ 'font-size': '3vh', color: 'white' }"
              class="text-center"
            >
              3. 이미지의 완성도입니다.<br />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="changeQuery(3)"
              />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="changeQuery(5)"
              />
            </div>
            <div
              v-if="page == 5"
              :style="{ 'font-size': '3vh', color: 'white' }"
              class="text-center"
            >
              4. 정답을 입력할 수 있는 칸입니다.<br />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="changeQuery(4)"
              />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="changeQuery(6)"
              />
            </div>
            <div
              v-if="page == 6"
              :style="{ 'font-size': '3vh', color: 'white' }"
              class="text-center"
            >
              5. 남은 물감의 총량입니다.<br />
              그림을 그리면서 물감이 소모되며, 소진 시 미션 실패로 게임이
              종료됩니다.<br />
              <v-btn
                class="ma-2"
                icon="mdi-arrow-left-bold"
                variant="text"
                @click="changeQuery(5)"
              />
              <!-- <v-btn
                class="ma-2"
                icon="mdi-arrow-right-bold"
                variant="text"
                @click="moveHome"
              /> -->
            </div>
          </v-container>
        </v-overlay>
      </v-overlay>
    </v-overlay>
  </v-app>
</template>
<script>
export default {
  props: ["page"],
  data() {
    return {
      audioInfo: !this.$root.audio.muted,
      overlay: false,
      totalTimer: 25,
    };
  },

  mounted() {
    this.overlay = true;
  },
  methods: {
    changeQuery(next) {
      this.$router.replace({ query: { page: next } });
    },
    moveHome() {
      this.$router.push({ path: "/" });
    },
    audioChange() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioInfo = !this.audioInfo;
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
.overlayedbar {
  transform: rotate(90deg);
  margin-top: 17vh;
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
  transform: rotate(90deg);
  margin-top: 17vh;
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

.nums {
  font-family: "num";
  font-size: 4rem;
}
</style>
