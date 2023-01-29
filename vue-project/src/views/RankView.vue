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

      <v-row class="justify-center nums" :style="{ 'margin-top': '10vh' }">
        <v-col cols="1">
          <profile />
        </v-col>

        <v-col cols="3"> Nask </v-col>
      </v-row>

      <v-row
        class="justify-center"
        :style="{ 'margin-top': '2vh', 'margin-bottom': '0vh' }"
      >
        <v-col cols="1" :style="{ 'margin-left': '30vw' }">
          <check />
        </v-col>
        <v-col cols="3" class="nums"> {{ correctAnswers }}/9 </v-col>
        <v-col
          cols="4"
          class="text-center"
          align-self="center"
          :style="{
            'font-size': '1vh',
            color: 'gold',
            overflow: 'hidden',
          }"
        >
          {{ rank }}
        </v-col>
      </v-row>

      <v-row class="justify-center nums" :style="{ 'margin-top': '0vh' }">
        <v-col cols="1">
          <timer />
        </v-col>
        <v-col cols="3">
          {{ clearTime }}
        </v-col>
      </v-row>

      <v-row>
        <v-btn
          class="mx-auto"
          :style="{ margin: '10vh 0vw 0vh 0vw' }"
          @click="goResult"
        >
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
      // rank: this.$store.state.rank
      rank: "A",
      clearTime: this.$store.state.clearTime.toString().substr(0, 5),
      correctAnswers: this.$store.state.correctAnswers,
      soundInfo: false,
      showInfo: false,
    };
  },
  methods: {
    goResult() {
      this.$router.push({ path: "/demoresult" });
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
