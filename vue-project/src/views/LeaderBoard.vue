<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class>
        <v-col cols="3" />
        <!-- ranking logo 출력 -->
        <v-col cols="6" class="d-flex justify-center align-center">
          <ranking class="rank" />
        </v-col>
      </v-row>

      <v-row class="d-flex d-sm-none justify-end">
        <!-- mobile portrait 음향 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!--mobile portrait 홈 버튼 -->
        <v-col cols="2" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-row
        class="d-none d-sm-flex justify-end"
        :style="{ margin: '3vh 0vw 0vh 0vw' }"
      >
        <!-- 음향 버튼 -->
        <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
          <v-icon :icon="audioIcon" size="5vh"> </v-icon>
        </v-btn>
      </v-row>

      <v-row
        class="d-none d-sm-flex justify-end"
        :style="{ margin: '3vh 0vw 0vh 0vw' }"
      >
        <!-- 홈 이동 버튼 -->
        <v-btn rounded variant="plain" @click="moveHome" height="5vh">
          <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>

      <v-row class="d-flex justify-center font">
        <!-- 랭킹 테이블 생성 -->
        <v-col xs="12" sm="6">
          <div class="scroll">
            <v-table class="table">
              <thead>
                <tr>
                  <th class="text-center">Name</th>
                  <th class="text-center">Score</th>
                  <th class="text-center">Time</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in ranking" :key="item.name">
                  <td class="text-center">{{ item.name }}</td>
                  <td class="text-center">{{ item.score }}</td>
                  <td class="text-center">{{ item.time }}</td>
                </tr>
              </tbody>
            </v-table>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import ranking from "../svg/rankingText.vue";
export default {
  components: {
    ranking,
  },
  data() {
    return {
      ranking: [
        { name: "a", score: "1", time: "1" },
        { name: "b", score: "2", time: "2" },
        { name: "c", score: "3", time: "3" },
        { name: "d", score: "4", time: "4" },
        { name: "e", score: "5", time: "5" },
        { name: "f", score: "6", time: "6" },
        { name: "g", score: "7", time: "7" },
        { name: "h", score: "8", time: "8" },
        { name: "i", score: "9", time: "9" },
        { name: "j", score: "10", time: "10" },
      ],
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
    };
  },
  methods: {
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
    moveHome() {
      this.$router.push({ path: "/" });
    },
  },
  async mounted() {
    if (this.$root.audio.paused) {
      this.$root.audio.play();
    }

    let response = await this.$api(
      "http://34.64.169.197/api/v1/score/read",
      "GET"
    );
    console.log(response);
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
}

.table {
  background-color: transparent;
}

@font-face {
  font-family: "default";
  src: url("../fonts/Lobster-Regular.ttf");
}

.font {
  font-family: "default";
  font-size: 2.3rem;
  color: white;
}

.scroll {
  max-height: calc(60vh);
  overflow-y: scroll;
}

@media only screen and (max-width: 480px) {
  .rank {
    margin-top: 0vh;
    margin-bottom: 0vh;
    width: 40vh;
  }
}

@media only screen and (min-width: 480px) {
  .rank {
    margin-top: 10vh;
  }
}
</style>
