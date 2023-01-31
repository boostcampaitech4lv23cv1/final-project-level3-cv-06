<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="d-flex justify-center">
        <logo :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-if="audioInfo == false">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-if="audioInfo == true">
          </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn
          rounded
          variant="plain"
          @click="movePage('/description', { page: 1 })"
        >
          <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>

      <v-row :style="{ margin: '30vh 0vw 0vh 0vw' }">
        <v-col cols="6">
          <v-btn
            rounded
            variant="plain"
            color="transparent"
            @click="movePage('/select')"
          >
            <game :style="{ height: '7vh' }" />
          </v-btn>
        </v-col>
        <v-col cols="6">
          <v-btn
            rounded
            variant="plain"
            color="transparent"
            @click="movePage('/transform')"
          >
            <transform :style="{ height: '7vh' }" />
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
import transform from "../svg/transformButton.vue";
import game from "../svg/GameButton.vue";

export default {
  data() {
    return {
      audioInfo: true,
    };
  },
  components: {
    logo,
    transform,
    game,
  },

  methods: {
    movePage(route, query) {
      this.$router.push({
        path: route,
        query: query,
      });
    },
    audioChange() {
      this.$root.audio.muted = !this.$root.audio.muted;
      if (this.audioInfo == true) {
        this.audioInfo = false;
      } else {
        this.audioInfo = true;
      }
    },
  },
  mounted() {
    this.$root.audio.play();
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
}
</style>
