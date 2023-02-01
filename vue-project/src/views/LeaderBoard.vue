<template>
  <v-app class="hero">
    <v-row class="d-flex justify-center">
      <ranking :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
    </v-row>
    <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
      <v-btn rounded variant="plain" @click="audioChange" height="5vh">
        <v-icon icon="mdi-volume-high" size="5vh" v-show="audioInfo == false">
        </v-icon>
        <v-icon icon="mdi-volume-off" size="5vh" v-show="audioInfo == true">
        </v-icon>
      </v-btn>
    </v-row>
    <v-row class="d-flex justify-center font">
      <v-col cols="4">
        <div class="scroll">
          <v-table class="table">
            <thead>
              <tr>
                <th class="text-center">Name</th>
                <th class="text-center">Score</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in ranking" :key="item.name">
                <td class="text-center">{{ item.name }}</td>
                <td class="text-center">{{ item.score }}</td>
              </tr>
            </tbody>
          </v-table>
        </div>
      </v-col>
    </v-row>
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
        { name: "a", score: "1" },
        { name: "b", score: "2" },
        { name: "c", score: "3" },
        { name: "d", score: "4" },
        { name: "e", score: "5" },
        { name: "f", score: "6" },
        { name: "g", score: "7" },
        { name: "h", score: "8" },
        { name: "i", score: "9" },
        { name: "j", score: "10" },
      ],
      audioInfo: !this.$root.audio.muted && !this.$root.audio.paused,
    };
  },
  methods: {
    audioChange() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioInfo = !this.audioInfo;
    },
  },
  // async mounted() {
  //     let response = await this.$api(
  //         'http://127.0.0.1:8000/api/v1/game/gameover',
  //         "POST",
  //     )
  // }
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
</style>
