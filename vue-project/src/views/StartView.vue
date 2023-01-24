<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="justify-center mt-10">
        <logo :style="{ height: '150px', width:  '600px' }" />
      </v-row>
      <v-row class="d-flex justify-end mt-10">
        <v-btn variant="text" v-bind="{ icon: soundIcon }" color="white" @click="soundChange"></v-btn>
      </v-row>

      <v-row class="d-flex justify-center align-center">
        <v-btn rounded variant="plain" @click='movePage("/select")'>
          <game :style="{ height: '80px', width: '180px' }" />
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center aligncenter mt-16">
        <v-btn rounded variant="plain" color="transparent" width="15%" @click='movePage("/transform")'>
          <transform :style="{ height: '80px', width: '200px' }" />
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center align-center buttons mt-16">
        <v-btn rounded variant="plain" color="transparent" width="15%"  @click='movePage("/description", { page: 1 })'>
          <description :style="{ height: '80px', width:'180px' }" />
        </v-btn>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import logo from '../svg/logoView.vue';
import transform from '../svg/transformButton.vue';
import game from '../svg/GameButton.vue';
import description from '../svg/descriptionButton.vue'

export default {
  components: {
    logo,
    transform,
    game,
    description,
  },
  data() {
    return {
      absolute: true,
      overlay: false,
      soundIcon: "mdi-volume-high",
      currentPage: 'page1'
    };
  },
  methods: {
    movePage(route, query) {
      this.$router.push({
        path: route,
        query: query
      })
    },
    soundChange() {
      if (this.soundIcon == 'mdi-volume-high') {
        this.soundIcon = 'mdi-volume-off'
      }
      else {
        this.soundIcon = 'mdi-volume-high'
      }

    }

  }
}
</script>

<style scoped>
.hero {
  background: url('../assets/background.png');
  background-size: cover;
  height: 100vh;
}


</style>