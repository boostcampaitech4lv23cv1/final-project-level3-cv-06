<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="d-flex justify-center">
        <logo :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '0vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="infoChange" height="5vh">
          <v-icon icon="mdi-information-outline" size="5vh"> </v-icon>
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-end" :style="{ margin: '3vh 0vw 0vh 0vw' }">
        <v-btn rounded variant="plain" @click="soundChange" height="5vh">
          <v-icon icon="mdi-volume-high" size="5vh" v-show="soundInfo == 0">
          </v-icon>
          <v-icon icon="mdi-volume-off" size="5vh" v-show="soundInfo == 1">
          </v-icon>
        </v-btn>
      </v-row>

      <v-row class="d-flex justify-center">
        <category :style="{ height: '7vh', margin: '0vh 0vw 5vh 0vw' }" />
      </v-row>

      <v-row class="d-flex justify-center">
        <v-radio-group v-model="selectedCategory">
          <v-btn
            rounded
            v-for="item in categoryItems"
            :key="item.value"
            :value="item.value"
            @click="changeCategory(item.value)"
            :class="{
              selected: selectedCategory === item.value,
              ' mx-auto ': true,
            }"
            :style="{ height: '5vh', width: '20vh', margin: '1vh 0vw 0vh 0vw' }"
          >
            {{ item.text }}
          </v-btn>
        </v-radio-group>
      </v-row>
      <v-col
        cols="12"
        class="d-flex justify-center"
        :style="{ margin: '3vh 0vw 0vh 0vw' }"
      >
        <v-btn :disabled="categoryIsEmpty" color="yellow" @click="startGame"
          >Game start</v-btn
        >
      </v-col>
    </v-container>
  </v-app>
</template>

<script>
import logo from "../svg/logoView.vue";
import category from "../svg/categoryView.vue";

export default {
  components: {
    logo,
    category,
  },
  data() {
    return {
      categoryItems: [
        { text: "Animal", value: "animal" },
        { text: "Landmark", value: "landmark" },
        { text: "Entertainment", value: "entertainer" },
      ],
      selectedCategory: "animal",
      soundInfo: false,
    };
  },
  computed: {
    categoryIsEmpty() {
      return this.selectedCategory === "";
    },
  },
  methods: {
    startGame() {
      this.$router.push({
        path: "/demo",
        query: { category: this.selectedCategory, mode: this.selectedMode },
      });
    },
    changeCategory(value) {
      this.selectedCategory = value;
    },
    soundChange() {
      if (this.soundInfo == true) {
        this.soundInfo = false;
      } else {
        this.soundInfo = true;
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
  background: url("../assets/test.jpg");
  background-size: cover;
  height: 100vh;
}
.selected {
  background-color: rgb(248, 207, 71);
}
</style>
