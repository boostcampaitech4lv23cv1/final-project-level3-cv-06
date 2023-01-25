<template>
    <v-app class="hero">
        <v-container>
            <v-row class="d-flex justify-center mt-16">
                <div :style="{ 'font-size': '30px', 'color': 'black' }" class="d-flex justify-center align-center">
                    Score</div>
            </v-row>
            <v-row>
                <F v-show="rank == 'F'" height="300" class="score-space mx-auto" />
                <S v-show="rank == 'S'" height="300" class="score-space mx-auto" />
            </v-row>

            <v-row>
                <v-btn class="mx-auto mt-16" @click="goResult">
                    Show Result! </v-btn>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
import F from '../svg/fRank.vue'
import S from '../svg/sRank.vue'

export default {
    components: {
        F,
        S,
    },
    data() {
        return {
            // rank: this.$store.state.rank
            rank: 'S'
        };
    },
    methods: {
        goResult() {
            this.$router.push({ path: '/demoresult' })
        }
    }
}
</script>

<style scoped>
.hero {
    background: url('../assets/back.jpg');
    background-size: cover;
    height: 100vh;
}

.score-space {
    margin-top: 150px;
}
</style>