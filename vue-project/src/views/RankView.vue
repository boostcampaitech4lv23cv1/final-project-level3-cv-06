<template>
  <v-app class="hero">
    <v-container>
      <v-row class="d-flex justify-center">
        <score :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '0vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="infoChange" height="5vh">
          <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="soundChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-show="soundInfo == 0">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-show="soundInfo == 1">
          </v-icon>
        </v-btn>
      </v-row>

      <v-row class="d-flex nums" :style="{ height: '30vh', 'margin-top': '3vh' }">
        <v-col cols="6" class="align-self-center">
          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
            <v-col cols="2" class="justify">
              <profile />
            </v-col>
            <v-col cols="3" class="justify"> Nask </v-col>
          </v-row>

          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
            <v-col cols="2">
              <check />
            </v-col>
            <v-col cols="3"> {{ correctAnswers }}/9 </v-col>
          </v-row>

          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
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
              'margin-left': '4vh',
              'margin-top': '5vh',
              'font-size': '23vh',
              color: 'gold',
            }">
              {{ rank }}
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <v-row class="d-flex">
        <v-btn class="mx-auto text-center" :style="{
          margin: '15vh 0vw 0vh 0vw',
        }" @click="goResult">
          Show Result!
        </v-btn>
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
      soundInfo: false,
      showInfo: false,
      correctNum: 0,
    };
  },

  methods: {
    goResult() {
      this.$router.push({ path: "/result" });
    },
    soundChange() {
      if (this.soundInfo == true) {
        this.soundInfo = false;
      } else {
        this.soundInfo = true;
      }
    },
    infoChange() {
      if (this.showInfo == true) {
        this.showInfo = false;
      } else {
        this.showInfo = true;
      }
    },
  },
  async mounted() {
    let correctList = this.$store.state.correctList
    let imgPath = this.$store.state.imgPath

    let response = await this.$api(
      "http://34.64.169.197/api/v1/game/gameover",
      "POST",
      { img_paths: imgPath, correct_list: correctList }
    );

    for (let i = 0; i < 9; i++) {
      if (correctList[i] == 1) {
        this.correctNum += 1
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
  <<<<<<< HEAD font-family: 'num';
  src: url('../fonts/Lobster-Regular.ttf')
}

.nums {
  font-family: 'num';
  =======font-family: "num";
  src: url("../fonts/Lobster-Regular.ttf");
}

.nums {
  font-family: "num";
  >>>>>>>65e7282dfb11b56bd491603e38de99c28995f77c font-size: 2.3rem;
}
</style>
