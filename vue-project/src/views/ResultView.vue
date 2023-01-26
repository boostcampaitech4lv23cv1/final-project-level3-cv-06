<template>
  <v-app class="">
    <v-container
      class="fill-height"
      fluid
      @click.stop
      :style="{ position: 'relative', backgroundColor: 'Lightcyan' }"
    >
      <v-row class="d-flex justify-center mt-16">
        <div
          :style="{ 'font-size': '50px', color: 'black' }"
          class="d-flex justify-center align-center"
        >
          Score
        </div>
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


            <v-row v-if="originImg != ''">
                <v-col v-for="n in 9" :key="n" class="d-flex child-flex no-padding" cols="4">
                    <v-img :width="350" :height="350" :src="`data:image/gif;base64,${result[n - 1]}`"
                        :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`" aspect-ratio="1" cover
                        class="grey lighten-2" @click="moveDetail(n)">
                    </v-img>
                </v-col>
            </v-row>

        </v-container>
    </v-app>
</template>

<script>
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
      rank: "C",
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
.score-space {
  margin-top: 150px;
}
</style>
