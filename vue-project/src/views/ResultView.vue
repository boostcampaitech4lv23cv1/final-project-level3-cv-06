<template>
  <v-app class="fill-height hero">
    <v-container>
      <v-row class=" justify-center">
        <result :style="{ height: '15vh', margin: '0vh 0vw 5vh 0vw' }" />
      </v-row>

      <v-row>
        <v-col v-for="n in 9" :key="n" class="d-flex child-flex no-padding" cols="4">
          <v-img :width="'20vw'" :height="'45vh'" :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1" cover :src="`data:image/gif;base64,${originImg[n - 1]}`" class="grey lighten-2"
            @click="moveDetail(n)">
          </v-img>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import result from '../svg/resultText.vue'
export default {
  components: {
    result,
  },
  data() {
    return {
      originImg: "",
    };
  },
  methods: {
    moveDetail(index) {
      this.$router.push({ path: "/demodetail", query: { index: index } });
    },
  },
  async mounted() {

  }
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
</style>
