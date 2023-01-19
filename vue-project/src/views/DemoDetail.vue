<template>
    <v-app>
        <v-container>
            <v-row class="d-flex child -flex mt-12 mb-12">
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
        }
    }
}
</script>