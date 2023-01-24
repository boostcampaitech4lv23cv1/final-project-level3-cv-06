<template>
    <v-app>
        <v-container>
            <v-row class="d-flex child -flex mt-10 mb-10">
                <div :style="{ 'font-size': '30px', 'color': 'black' }" class="mx-auto">Result</div>
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
export default {
    data() {
        return {
            originImg: this.$store.state.originImg,
            paintImg: this.$store.state.paintImg,
            answer: this.$store.state.answer,
            result: this.$store.state.result
        };
    },
    methods: {
        moveDetail(index) {
            this.$router.push({ path: '/detail', query: { index: index } })
        }
    }
}
</script>

<style scoped>
.no-padding {
    padding: 0;
}
</style>