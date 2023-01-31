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

      <v-row
        class="d-flex justify-center"
        :style="{ margin: '3vh 0vw 0vh 0vw' }"
      >
        <v-col cols="5">
          <v-img
            src="../assets/tower-bridge.jpg"
            height="25vh"
            width="25vw"
            class="mx-auto"
            v-show="uploaded == false"
          />
          <v-img
            max-height="25vh"
            class="mx-auto"
            max-width="25vw"
            :src="imageUrl"
            v-show="uploaded == true"
          />
        </v-col>
        <v-col cols="auto" class="d-flex align-center">
          <v-icon icon="mdi-arrow-right-bold" size="5vh"> </v-icon>
        </v-col>
        <v-col cols="5">
          <v-img
            src="../assets/tower-bridge-paint.jpg"
            height="25vh"
            width="25vw"
            class="mx-auto"
            v-show="uploaded == false"
          />

          <v-img
            max-height="25vh"
            class="mx-auto"
            max-width="25vw"
            :src="`data:image/gif;base64,${returnImg}`"
          >
            <v-progress-circular
              v-if="transform == true"
              class="loading"
              color="grey-lighten-4"
              indeterminate
            ></v-progress-circular>
          </v-img>
        </v-col>
      </v-row>
      <v-row :style="{ margin: '5vh 0vw 0vh 0vw' }">
        <v-col cols="6" class="mx-auto">
          <v-file-input
            clearable
            label="Upload your own image!"
            variant="solo"
            v-on:change="setImg"
          ></v-file-input>
          <!-- <input type="file" v-on:change="setImg" /> -->
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center">
        <v-col cols="auto">
          <v-btn @click="transformImg" :disabled="image == null"
            >Transform!</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
export default {
  components: {
    logo,
  },
  data() {
    return {
      image: null,
      transform: false,
      returnImg: null,
      img_loaded: false,
      soundInfo: false,
      uploaded: false,
      imageUrl: "",
      audioInfo: !this.$root.audio.muted,
    };
  },
  computed: {},
  methods: {
    setImg(event) {
      this.image = event.target.files[0];
      this.uploaded = true;
      this.imageUrl = URL.createObjectURL(this.image);
    },

    async transformImg() {
      // this.returnImg = null

      this.transform = true;
      const formData = new FormData();
      formData.append("file", this.image);

      let response = await this.$api2(
        "http://34.64.169.197/api/v1/infer",
        "POST",
        formData
      );
      // let response = await this.$api2(
      //   "http://127.0.0.1:8000/api/v1/infer",
      //   "POST",
      //   formData
      // );
      this.returnImg = response["image"];
      this.transform = false;
    },
    audioChange() {
      this.$root.audio.muted = !this.$root.audio.muted;
      if (this.audioInfo == true) {
        this.audioInfo = false;
      } else {
        this.audioInfo = true;
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

<style>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.loading {
  margin-top: 10vh;
  margin-left: 10vw;
}
</style>
