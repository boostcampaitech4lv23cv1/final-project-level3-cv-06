<template>
  <v-app>
    <v-container
      class="fill-height"
      fluid
      @click.stop
      :style="{ position: 'relative', backgroundColor: 'Lightcyan' }"
    >
      <div
        :style="{ 'font-size': '50px', color: 'black' }"
        class="d-flex justify-center align-center"
      >
        <paint width="50" class="mr-2" /> Save Paint!
      </div>
      <v-row class="d-flex justify-end mt-10">
        <v-btn
          variant="text"
          v-bind="{ icon: soundIcon }"
          color="black"
          @click="soundChange"
        ></v-btn>
      </v-row>

      <v-row class="d-flex justify-end">
        <v-btn
          variant="text"
          v-bind="{ icon: infoIcon }"
          color="black"
          @click="infoChange"
        ></v-btn>
      </v-row>

      <!-- <div>
        <v-img
          class="mx-auto"
          src="../assets/intro.gif"
          height="500"
          width="500"
        />
      </div> -->
      <v-row class="d-flex justify-center align-center buttons mt-0">
        <v-btn
          variant="flat"
          color="red"
          width="15%"
          @click="movePage('/select')"
        >
          Game Start
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center aligncenter mt-6">
        <v-btn
          variant="flat"
          color="yellow"
          width="15%"
          class="text-white"
          @click="movePage('/transform')"
        >
          Paint My Image
        </v-btn>
      </v-row>
      <v-row class="justify-center mt-16" v-show="showInfo == 1">
        <v-col cols="auto">
          <v-card height="250">
            <v-toolbar
              color="black"
              :style="{ 'font-size': '30px', color: 'black' }"
            >
              <v-icon>mdi-information-outline</v-icon></v-toolbar
            >

            <v-card-text :style="{ 'font-size': '20px', color: 'black' }">
              태일이는 내일 로봇 그림 경진대회에 참가할 예정입니다.<br /><br />
              작품 출품 전 미리 로봇의 성능을 테스트 하기 위해, 로봇이 제시어에
              맞는 이미지를 생성하는지 확인해야 합니다.<br /><br />
              물감이 부족한 태일이를 도와,
              <u>생성되는 그림을 보고 제시어를 빨리 맞혀주세요!</u>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                :style="{ background: 'gray' }"
                outlined
                id="click"
                background="red"
                backgroundColor="black"
                @click="infoChange"
                >Ok</v-btn
              >
              <v-spacer></v-spacer>

              <v-btn
                :style="{ background: 'gray' }"
                class="red"
                outlined
                id="click"
                background="red"
                @click="movePage('/description', { page: 4 })"
              >
                Learn how to play
              </v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
            <v-card-actions> </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import Paint from "../svg/paiNt.vue";
export default {
  components: {
    Paint,
  },
  data() {
    return {
      absolute: true,
      overlay: false,
      soundIcon: "mdi-volume-high",
      currentPage: "page1",
      infoIcon: "mdi-information-outline",
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
      if (this.soundIcon == "mdi-volume-high") {
        this.soundIcon = "mdi-volume-off";
      } else {
        this.soundIcon = "mdi-volume-high";
      }
    },
    infoChange() {
      if (this.infoIcon == "mdi-information-outline") {
        this.infoIcon = "mdi-arrow-left";
        this.showInfo = true;
      } else {
        this.infoIcon = "mdi-information-outline";
        this.showInfo = false;
      }
    },
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/Rectangle 2.jpg");
  background-size: cover;
  height: 100vh;
}

.buttons {
  margin-top: 400px;
}
</style>
