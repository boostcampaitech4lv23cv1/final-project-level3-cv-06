<template>
  <v-app class="hero">
    <v-container>
      <v-row class="justify-center mt-10">
        <score :style="{ height: '150px', width: '600px' }" />
      </v-row>
      <v-row>
        <Sstar
          v-show="rank == 'S'"
          height="100"
          class="score-space mx-auto mb-0"
        />
        <Astar
          v-show="rank == 'A'"
          height="100"
          class="score-space mx-auto mb-0"
        />
        <Bstar
          v-show="rank == 'B'"
          height="100"
          class="score-space mx-auto mb-0"
        />
        <Cstar
          v-show="rank == 'C'"
          height="100"
          class="score-space mx-auto mb-0"
        />
      </v-row>
      <v-row>
        <S v-show="rank == 'S'" height="300" class="score-space mx-auto mt-3" />
        <A v-show="rank == 'A'" height="300" class="score-space mx-auto mt-3" />
        <B v-show="rank == 'B'" height="300" class="score-space mx-auto mt-3" />
        <C v-show="rank == 'C'" height="300" class="score-space mx-auto mt-3" />
        <F v-show="rank == 'F'" height="300" class="score-space mx-auto" />
      </v-row>

      <v-row>
        <v-btn class="mx-auto mt-16" @click="goResult"> Show Result! </v-btn>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import score from "../svg/scoreView.vue";
import F from "../svg/fRank.vue";
import S from "../svg/sRank1.vue";
import A from "../svg/aRank.vue";
import B from "../svg/bRank.vue";
import C from "../svg/cRank.vue";
import Sstar from "../svg/sStar.vue";
import Astar from "../svg/aStar.vue";
import Bstar from "../svg/bStar.vue";
import Cstar from "../svg/cStar.vue";
export default {
  components: {
    score,
    F,
    S,
    A,
    B,
    C,
    Sstar,
    Astar,
    Bstar,
    Cstar,
  },
  data() {
    return {
      // rank: this.$store.state.rank
      rank: "S",
    };
  },
  methods: {
    goResult() {
      this.$router.push({ path: "/demoresult" });
    },
  },
};
</script>

<style scoped>
.hero {
  background: url("../assets/test.jpg");
  background-size: cover;
}

.score-space {
  margin-top: 150px;
}
</style>
