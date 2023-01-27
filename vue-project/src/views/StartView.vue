<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="justify-center">
        <logo :style="{ height: '35vh', width: '35vw' }" />
      </v-row>
      <!-- <v-row class="d-flex justify-end mt-10">
        <v-btn variant="text" v-bind="{ icon: soundIcon }" color="white" @click="soundChange"></v-btn>
      </v-row> -->

      <v-row class="d-flex justify-center align-center buttons">
        <v-col cols="6" class="justify-center">
        <v-btn
          rounded
          variant="plain"
          color="transparent"
          @click="movePage('/select')"
        >
          <game :style="{ height: '20vh', width: '20vw', margin: '0vh 10vw' }" />
        </v-btn>
        </v-col>
        <v-col cols="6" class="justify-center">
        <v-btn
          rounded
          variant="plain"
          color="transparent"
          @click="movePage('/transform')"
        >
          <transform :style="{ height: '20vh', width: '20vw', margin: '0vh 10vw' }" />
        </v-btn>
        </v-col>
      </v-row>
   
    </v-container>
  </v-app>
</template>

<script>
import logo from '../svg/logoView.vue';
import transform from '../svg/transformButton.vue';
import game from '../svg/GameButton.vue';
// import description from '../svg/descriptionButton.vue'

export default {
  components: {
    logo,
    transform,
    game,
    // description,
  },
  data() {
    return {
      absolute: true,
      overlay: false,
      soundIcon: "mdi-volume-high",
      currentPage: "page1",

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
      if (this.soundIcon == "mdi-volume-high") {
        this.soundIcon = "mdi-volume-off";
      } else {
        this.soundIcon = "mdi-volume-high";
      }
    },
   
  },
};
</script>

<style scoped>
.hero {
  background: url('../assets/test.jpg');
  background-size: cover;
}

.buttons {
  margin-top: 17vh;
}
</style>
