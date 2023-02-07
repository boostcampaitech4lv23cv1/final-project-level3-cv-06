<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class>
        <v-col cols="3" />
        <!-- ranking logo 출력 -->
        <v-col cols="6" class="d-flex justify-center align-center">
          <ranking class="rank" :style="{ 'height': '10vh' }" />
        </v-col>
      </v-row>

      <v-row class="d-flex justify-end">
        <!-- mobile portrait 음향 버튼 -->
        <v-col cols="2" sm="1" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="changeAudio" height="5vh">
            <v-icon :icon="audioIcon" size="5vh"> </v-icon>
          </v-btn>
        </v-col>

        <!--mobile portrait 홈 버튼 -->
        <v-col cols="2" sm="1" class="d-flex justify-center">
          <v-btn rounded variant="plain" @click="moveHome" height="5vh">
            <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center">
        <v-col cols="12" sm="6">
          <v-select v-model="category" :items="items"></v-select>
        </v-col>
      </v-row>

      <v-row class="d-flex justify-center font">
        <!-- 랭킹 테이블 생성 -->
        <v-col xs="12" sm="6">
          <div class="scroll">
            <v-table class="table">
              <thead>
                <tr>
                  <th class="text-center">Name</th>
                  <th class="text-center">Correct</th>
                  <th class="text-center">Time</th>
                  <th class="text-center">Score</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in ranking" :key="item.name">
                  <td class="text-center">{{ item.user_name }}</td>
                  <td class="text-center">{{ item.correct_cnt }}</td>
                  <td class="text-center">{{ parseInt(item.play_time / 60) }}m {{ parseInt(item.play_time % 60) }}s</td>
                  <td class="text-center">{{ item.score }}</td>
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
      ranking: [],
      items: ['animal', 'landmark', 'pokemon', 'celebrity'],
      category: 'animal',
      audioIcon: this.$root.audio.muted ? "mdi-volume-off" : "mdi-volume-high",
      score: this.$store.score
    };
  },
  methods: {
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
    moveHome() {
      this.$router.push({ path: "/" });
    },
  },
  async mounted() {
    let response = await this.$api(
      "http://34.64.169.197/api/v1/score/read?category=" + this.category,
      "GET",
    );
    this.ranking = response;
  },
  watch: {
    category: {
      immediate: true,
      handler: async function () {
        let response = await this.$api(
          "http://34.64.169.197/api/v1/score/read?category=" + this.category,
          "GET",
        );
        this.ranking = response
      }
    }
  }
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
  src: url("../fonts/BMJUA_ttf.ttf");
}

.font {
  font-family: "default";
  font-size: 1.2rem;
  color: white;
}

.scroll {
  max-height: calc(40vh);
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
