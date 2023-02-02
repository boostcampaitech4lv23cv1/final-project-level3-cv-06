<template>
  <v-app class="hero fill-height">
    <!-- <v-container class="d-none d-sm-block"> -->
    <v-container v-if="isPortrait == false">
      <v-row>
        <v-col cols="12" class="d-flex justify-center">
          <logo :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="audioChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-if="audioInfo == true">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-if="audioInfo == false">
          </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="moveHome" height="5vh">
          <v-icon icon="mdi-home-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <div class="text-center">
          <v-dialog v-model="dialog">
            <template v-slot:activator="{ props }">
              <v-btn rounded variant="plain" v-bind="props" height="5vh">
                <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title class="text-center" height="3vh"
                >변환하려는 이미지를 업로드하면, 그림으로 다시 그려드려요!
              </v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn variant="tonal" color="primary" @click="dialog = false"
                  >확인</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </div>
      </v-row>

      <v-row
        class="d-flex justify-center"
        :style="{ margin: '2vh 0vw 0vh 0vw' }"
      >
        <v-col cols="5">
          <v-img
            src="../assets/tower-bridge.jpg"
            width="30vw"
            class="mx-auto"
            v-show="uploaded == false"
          />
          <v-img
            max-height="25vh"
            class="mx-auto"
            max-width="30vw"
            :src="imageUrl"
            v-show="uploaded == true"
          />
        </v-col>
        <v-col cols="2" class="d-flex align-center justify-center">
          <v-icon icon="mdi-arrow-right-bold" size="5vh"> </v-icon>
        </v-col>
        <v-col cols="5">
          <v-img
            src="../assets/tower-bridge-paint.jpg"
            width="30vw"
            class="mx-auto"
            v-show="uploaded == false"
          />

          <v-img
            max-height="25vh"
            class="mx-auto"
            max-width="30vw"
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
        <v-col xs="12" sm="6" class="mx-auto">
          <v-file-input
            clearable
            label="Upload your own image!"
            variant="solo"
            v-on:change="setImg"
            density="compact"
          ></v-file-input>
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

    <!-- <v-container class="d-sm-none"> -->
    <v-container v-if="isPortrait == true">
      <v-row>
        <v-col cols="12" class="d-flex justify-center">
          <logo :style="{ width: '90vw', margin: '1vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>

      <v-row :style="{ margin: '1vh 0vw 0vh 0vw' }">
        <v-col cols="12">
          <v-file-input
            clearable
            label="Upload your own image!"
            variant="solo"
            v-on:change="setImg"
            density="compact"
          ></v-file-input>
        </v-col>
        <v-row class="d-flex justify-center">
          <v-col cols="auto">
            <v-btn @click="transformImg" :disabled="image == null"
              >Transform!</v-btn
            >
          </v-col>
        </v-row>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          class="d-flex justify-center"
          :style="{ margin: '5vh 0vw 0vh 0vw' }"
        >
          <v-img
            src="../assets/tower-bridge-paint.jpg"
            width="100vw"
            v-show="uploaded == false"
          />

          <v-img
            max-width="100vw"
            class="mx-auto"
            :src="`data:image/gif;base64,${returnImg}`"
          >
            <v-progress-circular
              v-if="transform == true"
              class="loading-mobile"
              color="grey-lighten-4"
              indeterminate
            ></v-progress-circular>
          </v-img>
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
      uploaded: false,
      imageUrl: "",
      audioInfo: !this.$root.audio.muted && !this.$root.audio.paused,
      dialog: false,
      isPortrait: true,
    };
  },
  mounted() {
    this.checkOrientation();
    window.addEventListener("orientationchange", this.checkOrientation);
  },
  beforeUnmount() {
    window.removeEventListener("orientationchange", this.checkOrientation);
  },
  methods: {
    checkOrientation() {
      this.isPortrait = window.screen.orientation.type === "portrait-primary";
    },
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

      // let response = await this.$api2(
      //   "http://34.64.169.197/api/v1/infer",
      //   "POST",
      //   formData
      // );

      let response = await this.$api2(
        "http://127.0.0.1:8000/api/v1/infer",
        "POST",
        formData
      );
      this.returnImg = response["image"];
      this.transform = false;
    },
    audioChange() {
      if (this.$root.audio.paused) {
        this.$root.audio.play();
      } else {
        this.$root.audio.muted = !this.$root.audio.muted;
      }
      this.audioInfo = !this.audioInfo;
    },
    moveHome() {
      this.$router.push({ path: "/" });
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

.loading-mobile {
  margin-top: 15vh;
  margin-left: 40vw;
}
</style>
