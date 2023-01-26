<template>
  <v-app class="hero">
    <v-container v-if="page < 4" class="hero" fluid>
      <v-row class="justify-center mt-16">
        <div
          v-if="page == 1"
          height="1"
          :style="{ 'font-size': '30px', color: 'white', position: '' }"
          class="text-center"
        >
          태일이는 내일 로봇 그림 경진대회에 참가할 예정입니다.<br />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-left-bold"
            variant="text"
            @click="moveHome"
          />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-right-bold"
            variant="text"
            @click="changeQuery(2)"
          />
        </div>
        <div
          v-if="page == 2"
          height="1"
          :style="{ 'font-size': '30px', color: 'white', position: '' }"
          class="text-center"
        >
          작품 출품 전 미리 로봇의 성능을 테스트하기 위해, 로봇이 제시어에 맞는
          이미지를 생성하는지 확인해야 합니다.<br />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-left-bold"
            variant="text"
            @click="changeQuery(1)"
          />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-right-bold"
            variant="text"
            @click="changeQuery(3)"
          />
        </div>
        <div
          v-if="page == 3"
          height="1"
          :style="{ 'font-size': '30px', color: 'white', position: '' }"
          class="text-center"
        >
          물감이 부족한 태일이를 도와주세요. 생성되는 그림을 보고 제시어를 빨리
          맞혀야합니다!
          <br />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-left-bold"
            variant="text"
            @click="changeQuery(2)"
          />
          <v-btn
            class="ma-2"
            icon="mdi-arrow-right-bold"
            variant="text"
            @click="changeQuery(4)"
          />
        </div>
      </v-row>
    </v-container>
    <v-container
      v-if="page > 3"
      class="fill-height"
      fluid
      @click.stop
      :style="{ position: 'relative', backgroundColor: 'gray' }"
    >
      >
      <v-row class="d-flex justify-center">
        <div
          v-if="page == 5"
          height="500px"
          :style="{ 'font-size': '50px', color: 'white', position: '' }"
          class="text-center"
        >
          4/9
        </div>
        <div
          v-else
          height="500px"
          :style="{ 'font-size': '50px', color: 'black', position: '' }"
          class="text-center"
        >
          4/9
        </div>
      </v-row>
      <v-row justify="space-between">
        <v-spacer></v-spacer>
        <v-col cols="4">
          <div v-if="page == 6" class="text-center">
            <v-img
              class="mx-auto"
              src="../assets/hanjimin.jpg"
              height="350"
              width="350"
            />
          </div>
          <div v-else>
            <v-img
              class="mx-auto"
              src="../assets/hanjimin_overlayed.jpg"
              height="350"
              width="350"
            />
          </div>
        </v-col>
        <v-col cols="4">
          <div v-if="page == 9" class="text-center mx-auto">
            <v-img src="../assets/total_timer.jpg" height="400" width="200" />
          </div>
          <div v-else class="text-center mx-auto">
            <v-img
              class=""
              src="../assets/total_timer_overlayed.jpg"
              height="400"
              width="200"
            />
          </div>
        </v-col>
      </v-row>
      <v-row class="mb-16">
        <v-spacer></v-spacer>
        <v-col cols="4">
          <div v-if="page == 7">
            <v-img
              class="mx-auto"
              src="../assets/img_timer.jpg"
              height="7"
              width="500"
            />
          </div>
          <div v-else class="mx-auto">
            <v-img
              class="mx-auto"
              src="../assets/img_timer_overlayed.jpg"
              height="7"
              width="500"
            />
          </div>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>

      <v-row class="mt-16 mb-16 justify-center">
        <v-col cols="4">
          <div v-if="page == 8" style="background-color: ghostwhite">
            <v-text-field
              hide-details="auto"
              readonly
              label="Answer"
            ></v-text-field>
          </div>
          <div v-else>
            <v-text-field
              backgroundColor="white"
              hide-details="auto"
              readonly
              label="Answer"
            ></v-text-field>
          </div>
        </v-col>
      </v-row>
      <!-- <v-row justify="center">
      <div
        v-if="page == 1"
        height="1"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        태일이는 내일 로봇 그림 경진대회에 참가할 예정입니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="moveHome"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(2)"
        />
      </div>
      <div
        v-if="page == 2"
        height="1"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        작품 출품 전 미리 로봇의 성능을 테스트하기 위해, 로봇이 제시어에 맞는
        이미지를 생성하는지 확인해야 합니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(1)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(3)"
        />
      </div>
      <div
        v-if="page == 3"
        height="1"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        물감이 부족한 태일이를 도와주세요. 생성되는 그림을 보고 제시어를 빨리
        맞혀야합니다!
        <br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(2)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(4)"
        />
      </div> -->
      <div
        v-if="page == 4"
        height="1"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        게임 화면의 구성을 설명합니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(3)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(5)"
        />
      </div>
      <div
        v-else-if="page == 5"
        height="500"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        1.현재 진행중인 게임 라운드입니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(4)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(6)"
        />
      </div>
      <div
        v-else-if="page == 6"
        height="500"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        2.현재 라운드에 해당하는 이미지를 생성합니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(5)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(7)"
        />
      </div>
      <div
        v-else-if="page == 7"
        height="500"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        3. 이미지의 완성도입니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(6)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(8)"
        />
      </div>
      <div
        v-else-if="page == 8"
        height="500"
        :style="{ 'font-size': '30px', color: 'white', position: '' }"
        class="text-center"
      >
        4. 정답을 입력할 수 있는 칸입니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(7)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="changeQuery(9)"
        />
      </div>
      <div
        v-if="page == 9"
        :style="{ 'font-size': '30px', color: 'white' }"
        class="text-center"
      >
        5. 남은 물감의 양입니다. 그림을 그리면서 물감이 소모되며, 소진 시 미션
        실패로 게임이 종료됩니다.<br />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-left-bold"
          variant="text"
          @click="changeQuery(8)"
        />
        <v-btn
          class="ma-2"
          icon="mdi-arrow-right-bold"
          variant="text"
          @click="moveHome"
        />
      </div>
    </v-container>
  </v-app>
</template>
<script>
export default {
  props: ["page"],
  data() {
    return {};
  },
  methods: {
    changeQuery(next) {
      this.$router.replace({ query: { page: next } });
    },
    moveHome() {
      this.$router.push({ path: "/" });
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
