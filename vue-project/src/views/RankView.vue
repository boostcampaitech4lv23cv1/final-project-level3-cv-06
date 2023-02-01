<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="d-flex justify-center">
        <score :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
      </v-row>

      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-show="audioInfo == false">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-show="audioInfo == true">
          </v-icon>
        </v-btn>
      </v-row>
      <v-row>
        <v-col cols="6" class="d-flex justify-end">
          <v-alert
            v-show="alert == true"
            density="compact"
            type="warning"
            style="position: absolute"
            width="17vw"
          >
            Enter your <strong>Name</strong>
          </v-alert>
        </v-col>
      </v-row>

      <v-row
        class="d-flex nums"
        :style="{ height: '30vh', 'margin-top': '0vh' }"
      >
        <v-col cols="6" class="align-self-center">
          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '0vh', 'font-size': '4vh' }">
            <v-col cols="2" class="justify">
              <profile />
            </v-col>
            <!-- <v-col cols="3" class="justify"> Nask </v-col> -->
            <v-col cols="3" class="justfy">
              <v-text-field
                label="Enter your name here!"
                v-model="name"
                single-line
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row
            class="d-flex justify-end"
            :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }"
          >
            <v-col cols="2">
              <check />
            </v-col>
            <v-col cols="3"> {{ correctAnswers }}/9 </v-col>
          </v-row>

          <v-row
            class="d-flex justify-end"
            :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }"
          >
            <v-col cols="2">
              <timer />
            </v-col>
            <v-col cols="3">
              {{ clearTime }}
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="6">
          <v-row>
            <v-col cols="auto" :style="{
              'margin-left': '7vh',
              'margin-top': '2vh',
              'font-size': '23vh',
              color: 'gold',
            }">
              {{ rank }}
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center">
        <v-col cols="6" class="d-flex justify-cnter">
          <v-btn
            class="mx-auto text-center"
            :style="{
              margin: '15vh 0vw 0vh 0vw',
            }"
            @click="goResult"
          >
            Show Result!
          </v-btn>
          <v-btn
            class="mx-auto text-center"
            :style="{
              margin: '15vh 0vw 0vh 0vw',
            }"
            @click="registerScore"
          >
            Register Score!
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import timer from "../svg/timerView.vue";
import check from "../svg/rightAnswer.vue";
import score from "../svg/scoreText.vue";
import profile from "../svg/profileView.vue";

export default {
  components: {
    score,
    timer,
    check,
    profile,
  },
  data() {
    return {
      rank: "",
      clearTime: this.$store.state.clearTime.toString().substr(0, 5),
      correctAnswers: this.$store.state.correctAnswers,
      audioInfo: !this.$root.audio.muted && !this.$root.audio.paused,
      showInfo: false,
      correctNum: 0,
      name: this.$store.state.name,
      alert: false,
    };
  },

  methods: {
    goResult() {
      this.$router.push({ path: "/demoresult" });
    },
    audioChange() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioInfo = !this.audioInfo;
    },
    infoChange() {
      if (this.showInfo == true) {
        this.showInfo = false;
      } else {
        this.showInfo = true;
      }
    },
    async registerScore() {
      if (this.name === "") {
        this.alert = true
      }
      else {
        this.$store.commit('setName', this.name)
        this.$router.push({ path: 'leaderboard' })

        let response = await this.$api(
          "http://34.64.169.197/api/v1/score",
          "POST",
          { user_name: this.name, play_time: this.clearTime, correct_ctn: this.correctAnswers }
        );

      }
    },
  },
  async mounted() {
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
    } else if (Number(this.clearTime) <= 90) {
      this.rank = "C";
    }

    let response = await this.$api(
      "http://34.64.169.197/api/v1/game/gameover",
      "POST",
      { category: this.$store.category, img_paths: imgPath, correct_list: correctList }
    );


    // let response = await this.$api(
    //   'http://127.0.0.1:8000/api/v1/game/gameover',
    //   "POST",
    //   { img_paths: imgPath, score_list: correctList }
    // )

  }
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

.result {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
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
</style>
