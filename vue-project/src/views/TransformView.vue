<template>
  <v-app class="hero">
    <v-container>
      <v-row class="mt-16">
        <v-col cols="8" class="mx-auto">
          <v-file-input
            clearable
            label="File input"
            variant="solo"
            v-on:change="setImg"
          ></v-file-input>
          <!-- <input type="file" v-on:change="setImg" /> -->
        </v-col>
        <v-col cols="2" class="align-center mt-2">
          <v-btn @click="transformImg" :disabled="image == null"
            >Transform!</v-btn
          >
        </v-col>
      </v-row>
      <v-row class="mt-16">
        <v-img
          max-height="400"
          class="mx-auto"
          max-width="400"
          :src="`data:image/gif;base64,${returnImg}`"
        >
          <v-progress-circular
            v-show="transform == true"
            class="loading"
            color="grey-lighten-4"
            indeterminate
          ></v-progress-circular>
        </v-img>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      image: null,
      transform: false,
      returnImg: null,
      img_loaded: false,
    };
  },
  computed: {},
  methods: {
    setImg(event) {
      this.image = event.target.files[0];
    },

    async transformImg() {
      // this.returnImg = null
      this.transform = true;
      const formData = new FormData();
      formData.append("file", this.image);

      let response = await this.$api2(
        "http://127.0.0.1:8000/api/v1/infer",
        "POST",
        formData
      );
      this.returnImg = response["image"];
      this.transform = false;
    },
  },
};
</script>

<style>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.loading {
  margin-top: 150px;
  margin-left: 200px;
}
</style>
