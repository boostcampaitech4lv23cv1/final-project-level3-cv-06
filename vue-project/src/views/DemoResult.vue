<template>
  <v-app>
    <v-container>
      <v-row class="d-flex child -flex mt-10 mb-10">
        <div :style="{ 'font-size': '30px', color: 'black' }" class="mx-auto">
          Result
        </div>
      </v-row>

      <v-row>
        <v-col
          v-for="n in 9"
          :key="n"
          class="d-flex child-flex no-padding"
          cols="4"
        >
          <v-img
            :width="350"
            :height="350"
            :src="`data:image/gif;base64,${originImg[n - 1]}`"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            cover
            class="grey lighten-2"
            @click="moveDetail(n)"
          >
          </v-img>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      originImg: "",
      imgList: this.$store.state.imgList,
    };
  },
  methods: {
    moveDetail(index) {
      this.$router.push({ path: "/demodetail", query: { index: index } });
    },
  },
  async mounted() {
    let response = await axios.post(
      "http://127.0.0.1/api/v1/game/result",
      { paths: this.imgList },
      { "Content-Type": "application/json" }
    );
    this.originImg = response.data.origin_imgs;

    this.$store.commit("setOrigin", response.data.origin_imgs);
    this.$store.commit("setResult", response.data.result_imgs);
  },
};
</script>

<style scoped>
.no-padding {
  padding: 0;
}
</style>
