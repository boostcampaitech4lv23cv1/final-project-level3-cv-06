<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="d-flex justify-center">
        <logo :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
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
  components: {
    logo,
    transform,
    game,
  },
  data() {
    return {
      absolute: true,
      overlay: false,
      soundInfo: false,
      currentPage: "page1",
      showInfo: false,
    };
  },
  methods: {
    movePage(route, query) {
      this.$router.push({
        path: route,
        query: query,
      });
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
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
}

.buttons {
  margin-top: 17vh;
}
</style>
