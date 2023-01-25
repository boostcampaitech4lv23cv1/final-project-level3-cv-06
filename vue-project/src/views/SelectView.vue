<template>
  <v-app class="hero">
    <v-container height="100%">
      <v-row class="justify-center mt-16">
        <logo :style="{ height: '150px', width: '600px' }" />
      </v-row>
      <v-row class="buttons">
        <v-col cols="6" class="d-flex justify-center align-end">
          <mode :style="{ height: '50px', width: '150px' }" />
        </v-col>
        <v-col cols="6" class="d-flex justify-center align-end">
          <category :style="{ height: '50px', width: '230px' }" />
        </v-col>
      </v-row>
      <v-row>
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
      </v-row>
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

export default {
  components: {
    logo,
    mode,
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
      selectedMode: "painttransformer",
      modeItems: [{ text: "Paint Transformer", value: "painttransformer" }],
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
