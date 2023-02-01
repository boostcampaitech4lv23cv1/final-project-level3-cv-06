<template>
  <v-app class="fill-height hero">
    <v-container height="100%">
      <v-row class="justify-center">
        <result :style="{ height: '15vh', margin: '0vh 0vw 0vh 0vw' }" />
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 5vh 0vw' }">
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-if="audioInfo == true">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-if="audioInfo == false">
          </v-icon>
        </v-btn>
      </v-row>
      <v-row>
        <v-col
          v-for="n in 9"
          :key="n"
          class="d-flex child-flex no-padding"
          cols="4"
        >
          <v-img
            :width="'45vw'"
            :height="'60vh'"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            cover
            :src="`${originImg[n - 1]}`"
            class="grey lighten-2"
            @click="moveDetail(n - 1)"
          >
          </v-img>
        </v-col>
      </v-row>

      <v-dialog v-model="showDialog" max-height="75vh" max-width="100vw">
        <v-row>
          <v-col cols="4" class="mx-auto text-center nums">
            {{ answer[dialogNum] }}
          </v-col>
        </v-row>
        <v-row class="d-flex justify-center align-center">
          <v-col cols="4" class="d-flex justify-center align-center">
            <v-img :src="`${paintImg[dialogNum]}`" max-height="50vh" />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="1" class="mx-auto">
            <v-btn color="primary" block @click="showDialog = false"
              >Close</v-btn
            >
          </v-col>
        </v-row>
      </v-dialog>
    </v-container>
  </v-app>
</template>

<script>
import result from "../svg/resultText.vue";
export default {
  components: {
    result,
  },
  data() {
    return {
      originImg: this.$store.state.originImg,
      resultImg: this.$store.state.paintImg,
      showDialog: false,
      dialogNum: false,
      answer: this.$store.state.answerList,
      audioInfo: !this.$root.audio.muted && !this.$root.audio.paused,
    };
  },
  methods: {
    moveDetail(index) {
      this.dialogNum = index;
      this.showDialog = true;
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
  background: url("../assets/test.jpg");
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
}

.no-padding {
  padding: 0;
}

@font-face {
  font-family: "answer";
  src: url("../fonts/Lobster-Regular.ttf");
}

.nums {
  font-family: "answer";
  font-size: 2.3rem;
  color: white;
}
</style>
