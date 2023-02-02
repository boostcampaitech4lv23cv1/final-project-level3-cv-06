<template>
  <v-app class="hero">
    <v-container height="100%">


      <v-row class="d-flex justify-center">
        <!-- save paint! 로고 출력 -->
        <v-col cols="10" class="d-flex justify-center">
          <logo :style="{ height: '14vh', margin: '10vh 0vw 0vh 0vw' }" />
        </v-col>
      </v-row>


      <v-row :style="{ margin: '20vh 0vw 0vh 0vw' }">
        <!-- 게임 버튼 select 페이지로 이동  -->
        <v-col cols="6" class="d-flex justify-center">
          <v-btn rounded variant="plain" color="transparent" @click="movePage('/select')">
            <game :style="{ height: '7vh' }" />
          </v-btn>
        </v-col>

        <!-- 이미지 변환 페이지로 이동하는 버튼 -->
        <v-col cols="6" class="d-flex justify-center">
          <v-btn rounded variant="plain" color="transparent" @click="movePage('/transform')">
            <transform :style="{ height: '7vh' }" />
          </v-btn>
        </v-col>
      </v-row>


      <v-row :style="{ margin: '10vh 0vw 0vh 0vw' }" class="d-flex justify-center">
        <!-- 리더보드로(랭킹) 이동하는 버튼 -->
        <v-col cols="6" class="d-flex justify-center">
          <v-btn rounded variant="plain" color="transparent" @click="movePage('/leaderboard')">
            <ranking :style="{ height: '7vh' }" />
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>


<script>
import logo from "../svg/logoView.vue";
import transform from "../svg/transformButton2.vue";
import game from "../svg/GameButton.vue";
import ranking from "../svg/RankingLogo.vue";

export default {


  components: {
    logo,
    transform,
    game,
    ranking,
  },


  methods: {
    /** 
     * 버튼 클릭시 페이지 이동하는 함수
     * @function movePage
     * @param {string} route 이동할 페이지
    */
    movePage(route) {
      this.$router.push({
        path: route,
      });

    },
  },


};
</script>


<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
}
</style>
