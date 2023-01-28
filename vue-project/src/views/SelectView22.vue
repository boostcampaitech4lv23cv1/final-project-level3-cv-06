<template>
  <v-app class="hero">
    <v-container height="100%">
      
      <v-row class="justify-center">
        <logo :style="{ height: '20vh', width: '35vw', margin: '5vh 0vh 0vw 0vw'}" />
      </v-row>
         <v-row class="d-flex justify-end">
        <v-btn rounded variant="plain"  @click="infoChange"  >
          <v-icon icon="mdi-information-outline" size="x-large" >
          </v-icon>
          </v-btn>
        
        </v-row>
         <v-row class="d-flex justify-end">
        <v-btn variant="text" v-bind="{ icon: soundIcon }" color="gray" @click="soundChange" :style="{margin: '0vh 0.75vh 0vw 0vw'}" ></v-btn>
      </v-row>
      <v-row class="justify-center" v-show="showInfo == 1">
        <v-col cols="auto">
          <v-card height="250">
            <v-toolbar
              color="black"
              :style="{ color: 'black' }"
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
      <v-row>
        <v-col cols="4" class = "text-center">
          Animals
        </v-col>

        <v-col cols="4" class = "text-center">
          Celebs        </v-col>

        <v-col cols="4" class = "text-center">
          Landmarks
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4">
          <v-img
            src="../assets/tiger.jpg"
            max-height="30vh"
  max-width="10vw"
            class="mx-auto"
            @click="changeCategory(entertainer)"
            />
        </v-col>

        <v-col cols="4">
          <v-img
            src="../assets/200.jpg"

            max-height="30vh"
  max-width="10vw"
            class="mx-auto"
            @click="changeCategory(entertainer)"
            />
        </v-col>

        <v-col cols="4">
          <v-img
            src="../assets/tower.jpg"
            max-height="30vh"
  max-width="10vw"
            class="mx-auto"
            @click="changeCategory(entertainer)"
            />
        </v-col>

      
      </v-row>
      <!-- <v-row>
        <v-col cols="6">
          <v-radio-group v-model="selectedMode">
            <v-btn
              rounded
              v-for="item in modeItems"
              :key="item.value"
              :value="item.value"
              @click="changeMode(item.value)"
              :class="{
                selected: selectedMode === item.value,
                'mb-4 w-50 mx-auto ': true,

              }"
            >
              {{ item.text }}
            </v-btn>
          </v-radio-group>
        </v-col>
        <v-col cols="6">
          <v-radio-group v-model="selectedCategory">
            <v-btn
              rounded
              v-for="item in categoryItems"
              :key="item.value"
              :value="item.value"
              @click="changeCategory(item.value)"
              :class="{
                selected: selectedCategory === item.value,
                'mb-4 w-50 mx-auto ': true,

              }"
            >
              {{ item.text }}
            </v-btn>
          </v-radio-group>
        </v-col>
      </v-row> -->
      <v-col cols="12" class="d-flex justify-center mt-16">
        <v-btn :disabled="categoryIsEmpty" color="yellow" @click="startGame"
          >Game start</v-btn
        >
      </v-col>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
import mode from "../svg/modeView.vue";
import category from "../svg/categoryView.vue";
// import description from "../svg/descriptionButton.vue"
export default {
  components: {
    logo,
    // description,
  },
  data() {
    return {
      categoryItems: [
        { text: "Animal", value: "animal" },
        { text: "Landmark", value: "landmark" },
        { text: "Entertainment", value: "entertainer" },
      ],
      selectedCategory: "animal",
      soundIcon: "mdi-volume-high",
      modeItems: [{ text: "Paint Transformer", value: "painttransformer" }],
      showInfo: false,
    };
  },
  computed: {
    categoryIsEmpty() {
      return this.selectedCategory === "" || this.selectedMode === "";
    },
  },
  methods: {
    startGame() {
      this.$router.push({
        path: "/demo",
        query: { category: this.selectedCategory, mode: this.selectedMode },
      });
    },
    changeMode(value) {
      this.selectedMode = value;
    },
    changeCategory(value) {
      this.selectedCategory = value;
    },
    infoChange() {
      if (this.showInfo == true) {
        this.showInfo = false;
      } else {
        this.showInfo = true;
      }
    },
    soundChange() {
      if (this.soundIcon == "mdi-volume-high") {
        this.soundIcon = "mdi-volume-off";
      } else {
        this.soundIcon = "mdi-volume-high";
      }
    },
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}

.darken {
  filter: brightness(80%);
}

.selected {
  background-color: rgb(255, 196, 0);

}

.grey {
  background-color: #9e9e9e;
  color: #fff;
}

.buttons {
  margin-top: 80px;
}
</style>
