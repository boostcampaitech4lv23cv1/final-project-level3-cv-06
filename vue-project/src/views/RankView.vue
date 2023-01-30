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
      <v-row class="justify-center nums">
        <check />
        9/9
      </v-row>

      <v-row class="justify-center nums" :style="{ 'margin-top': '3vh' }">
        <timer />
        01:47
      </v-row>

      <v-row class="d-flex justify-center" :style="{ height: '25vh', margin: '0vh 0vw 0vh 0vw' }">
        <v-col cols="auto" align-self="start" :style="{
          'font-size': '25vh',
          color: 'gold',
          margin: '0vh 0vw 0vh 0vw',
        }">S</v-col>

        <v-col cols="auto" align-self="center">
          <v-div :style="{
            'font-size': '3vh',
            color: 'gray',
            margin: '0vh 0vw 0vh 0vw',
          }">
            rank
          </v-div>
        </v-col>
      </v-row>

      <v-row>
        <v-btn class="mx-auto" :style="{ margin: '10vh 0vw 0vh 0vw' }" @click="goResult">
          Show Result!
        </v-btn>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import timer from "../svg/timerView.vue";
import check from "../svg/rightAnswer.vue";
import score from '../svg/scoreText.vue'

export default {
  components: {
    score,
    timer,
    check,
  },
  data() {
    return {
      // rank: this.$store.state.rank
      rank: "A",
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
  }
};
</script>

<style scoped>
.s-rank {
  color: gold;
  align-self: "start";
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
  font-family: 'num';
  src: url('../fonts/Lobster-Regular.ttf')
}

.nums {
  font-family: 'num';
  font-size: 2.3rem;
}
</style>
