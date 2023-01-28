<template>
    <v-app class='hero'>
        <v-container>
            <v-row class="d-flex">
            </v-row>
            <v-row>
                {{ answer[index] }}
            </v-row>
            <v-row>
                <v-col cols=6>
                    <v-img :src="`data:image/gif;base64,${originImg[index - 1]}`" />
                </v-col>
                <v-col cols=6>
                    <v-img :src="`data:image/gif;base64,${paintImg[index - 1]}`" />
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            index: this.$route.query.index,
            originImg: this.$store.state.originImg,
            paintImg: this.$store.state.result,
            answer: this.$store.state.answer
        }
    }
}
</script>

<style>
.hero {
    background: url("../assets/test.jpg");
    background-size: cover;
    background-position: center;
    height: 100vh;
    width: 100vw;
}
</style>