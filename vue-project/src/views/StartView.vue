<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="justify-center mt-16">
        <logo :style="{ height: '150px', width: '600px' }" />
      </v-row>
      <!-- <v-row class="d-flex justify-end mt-10">
        <v-btn variant="text" v-bind="{ icon: soundIcon }" color="white" @click="soundChange"></v-btn>
      </v-row> -->

      <v-row class="d-flex justify-center align-center buttons">
        <v-btn
          rounded
          variant="plain"
          color="transparent"
          @click="movePage('/select')"
        >
          <game :style="{ height: '80px', width: '180px' }" />
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center aligncenter mt-16">
        <v-btn
          rounded
          variant="plain"
          color="transparent"
          @click="movePage('/transform')"
        >
          <transform :style="{ height: '80px', width: '180px' }" />
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center align-center buttons mt-16">
        <v-btn rounded variant="plain" color="transparent" @click="infoChange">
          <description :style="{ height: '80px', width: '180px' }" />
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
          </v-card>
        </v-col>
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
      if (this.soundIcon == "mdi-volume-high") {
        this.soundIcon = "mdi-volume-off";
      } else {
        this.soundIcon = "mdi-volume-high";
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
  background: url('../assets/test.jpg');
  background-size: cover;
}

.buttons {
  margin-top: 17vh;
}
</style>
