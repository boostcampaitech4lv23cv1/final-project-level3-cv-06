<template>
  <v-app class="hero">
    <v-container>

      <v-row>
        <!-- score log show -->
        <v-col cols="12" class="d-flex justify-center">
          <score :style="{ height: '15vh', margin: '5vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>


      <v-row class="d-flex justify-end" :style="{ margin: '0vh 0vw 0vh 0vw' }">
        <!-- description button as icon -->
        <v-btn rounded variant="plain" @click="infoChange" height="5vh">
          <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>


      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <!-- sound button as icon-->
        <v-btn rounded variant="plain" @click="soundChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-show="soundInfo == 0">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-show="soundInfo == 1">
          </v-icon>
        </v-btn>
      </v-row>


      <v-row class=" d-flex nums" :style="{ height: '30vh', 'margin-top': '0vh' }">
        <!-- game result information -->
        <v-col cols="6" class="align-self-center">
          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '0vh', 'font-size': '4vh' }">
            <!-- profile icon & name input -->
            <v-col cols="1" class="justify">
              <profile />
            </v-col>
            <!-- name input area -->
            <v-col cols="1"></v-col>
            <v-col xs="10" sm="5" lg="3" class="d-flex align-start">
              <v-text-field label="Enter name here!" v-model="name" single-line class="input"></v-text-field>
            </v-col>
          </v-row>


          <v-row class="d-flex justify-end" :style="{ height: '8vh', 'margin-top': '3vh', 'font-size': '4vh' }">
            <!-- check icon & correct number -->
            <v-col cols="1">
              <check />
            </v-col>
            <v-col cols="1"></v-col>
            <!-- correct answer number show -->
            <v-col xs="10" sm="5" lg="3" class="justfy"> {{ correctAnswer }}/9 </v-col>
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
          }" @click="registerScore">
            Show Rank
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
      correctAnswer: this.$store.state.correctAnswer,
      soundInfo: false,
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
    async registerScore() {
      if (this.name === "") {
        this.alert = true
      }
      else {
        this.$store.commit('setName', this.name)
        this.$router.push({ path: 'leaderboard' })

        // let response = await this.$api(
        //   "http://34.64.169.197/api/v1/score",
        //   "POST",
        //   { user_name: this.name, play_time: this.clearTime, correct_ctn: this.correctAnswer }
        // );

      }
    }
  },
  async mounted() {
    let correctList = this.$store.state.correctList
    let imgPath = this.$store.state.imgPath

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
    } else if (Number(this.clearTime) <= 100) {
      this.rank = "C";
    }

    // let response = await this.$api(
    //   "http://34.64.169.197/api/v1/game/gameover",
    //   "POST",
    //   { category: this.$store.category, img_paths: imgPath, correct_list: correctList }
    // );


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
  font-family: 'num';
  src: url('../fonts/Lobster-Regular.ttf')
}

.nums {
  font-family: 'num';
  font-size: 2.3rem;
}

.input {
  height: 1vh;
}
</style>
