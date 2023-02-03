<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row>
        <!-- score log show -->
        <v-col cols="12" class="d-flex justify-center">
          <score :style="{ height: '15vh', margin: '5vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>

      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-show="audioInfo == true">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-show="audioInfo == false">
          </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="moveHome" height="5vh">
          <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>

      <v-row class="d-flex align nums" :style="{ height: '30vh', 'margin-top': '0vh' }">
        <!-- game result information -->
        <v-col cols="6" class="align-self-center">
          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
            <!-- check icon & correct number -->
            <v-col cols="1">
              <check />
            </v-col>
            <v-col cols="1"></v-col>
            <!-- correct answer number show -->
            <v-col xs="10" sm="5" lg="3" class="justfy">
              {{ correctAnswer }}/9
            </v-col>
          </v-row>

          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
            <!--timer icon show & clear time-->
            <v-col cols="1">
              <timer />
            </v-col>
            <v-col cols="1"></v-col>
            <!--clear time show-->
            <v-col xs="10" sm="5" lg="3" class="justfy">
              {{ clearTime }}
            </v-col>
          </v-row>
        </v-col>

        <!-- show rank emoji -->
        <v-col cols="4" :style="{
          'margin-left': '7vh',
          'margin-top': '2vh',
          'font-size': '23vh',
          color: 'gold',
        }">
          {{ rank }}
        </v-col>
      </v-row>

      <v-row class="justify-center">
        <v-col cols="5" class="d-flex justify-end">
          <!-- go result button -->
          <v-btn class="text-center" :style="{
            margin: '15vh 0vw 0vh 0vw',
          }" @click="goResult">
            Show Result!
          </v-btn>
        </v-col>
        <v-col cols="1"></v-col>
        <v-col cols="5">
          <!-- register score and go leaderboard -->
          <v-btn class="text-center" :style="{
            margin: '15vh 0vw 0vh 0vw',
          }" @click="showDialog = true">
            Register!
          </v-btn>
        </v-col>
      </v-row>


      <v-dialog v-model="showDialog">
        <v-row class="d-flex justify-center">
          <v-col cols="12" sm="6">
            <v-card>
              <v-card-title> Register your score! </v-card-title>
              <v-divider class="mx-4 mb-1"></v-divider>
              <v-card-text>
                <v-text-field density="compact" label="Enter your name!" single-line v-model="name"></v-text-field>
              </v-card-text>
              <v-card-actions class="d-flex justify-end">
                <v-btn @click="registerScore"> Register </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>
  </v-app>
</template>

<script>
import timer from "../svg/timerView.vue";
import check from "../svg/rightAnswer.vue";
import score from "../svg/scoreText.vue";

export default {
  components: {
    score,
    timer,
    check,
  },
  data() {
    return {
      rank: "",
      clearTime: this.$store.state.clearTime.toString().substr(0, 5),
      correctAnswer: this.$store.state.correctAnswer,
      audioInfo: true,
      correctNum: 0,
      name: '',
      showDialog: false
    };
  },

  methods: {
    goResult() {
      this.$router.push({ path: "/demoresult" });
    },
    audioChange() {
      this.$root.audio.muted = !this.$root.audio.muted;
      this.audioInfo = !this.audioInfo;
    },
    moveHome() {
      this.$router.push({ path: "/" });
    },

    async registerScore() {
      this.$router.push({ path: "leaderboard" });

      let response = await this.$api(
        "http://34.64.169.197/api/v1/score/create",
        "POST",
        { user_name: this.name, play_time: this.clearTime, correct_cnt: this.correctAnswer }
      );
      this.name = ""
    },
  },
  async mounted() {
    this.$root.audio.play();
    this.audioInfo = !this.$root.audio.muted;
    let correctList = this.$store.state.correctList;
    let imgPath = this.$store.state.imgPath;

    for (let i = 0; i < 9; i++) {
      if (correctList[i] == 1) {
        this.correctNum += 1;
      }
    }
    if (Number(this.clearTime) <= 60) {
      this.rank = "S";
    } else if (Number(this.clearTime) <= 70) {
      this.rank = "A";
    } else if (Number(this.clearTime) <= 80) {
      this.rank = "B";
    } else if (Number(this.clearTime) <= 100) {
      this.rank = "C";
    }
  },
};
</script>

<style scoped>
.s-rank {
  color: gold;
  align-self: "start";
  font-size: "5em";
  width: "10vh";
  height: "10vh";
}

.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.score-space {
  margin-top: 150px;
}

@font-face {
  font-family: "num";
  src: url("../fonts/Lobster-Regular.ttf");
}

.nums {
  font-family: "num";
  font-size: 2.3rem;
}

.input {
  height: 1vh;
}
</style>
