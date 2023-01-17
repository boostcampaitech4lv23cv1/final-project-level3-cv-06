<template>
    <v-app class="hero">
        <v-container>
            <v-row class="mt-16">
                <v-col cols=8 class="mx-auto">
                    <v-file-input clearable label="File input" variant="solo" v-on:change='setImg'></v-file-input>
                    <!-- <input type="file" v-on:change="setImg" /> -->
                </v-col>
                <v-col cols="2" class="align-center mt-2">
                    <v-btn v-model="transform" @click='transformImg'>Transform!</v-btn>
                </v-col>
            </v-row>
            <v-row>
                <v-img class="mx-auto mt-16" max-height="400" max-width="400"
                    :src="`data:image/gif;base64,${returnImg}`" />
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            image: null,
            transform: false,
            returnImg: null,
            img_loaded: false,
        }
    },
    methods: {
        setImg(event) {
            this.image = event.target.files[0]
        },

        async transformImg() {
            const formData = new FormData();
            formData.append('file', this.image);

            let response = await this.$api2('http://127.0.0.1:8000/api/v1/infer', 'POST', formData)
            this.returnImg = response['pred']
        },
    }
}
</script>

<style>
.hero {
    background: url('../assets/back.jpg');
    background-size: cover;
    height: 100vh;
}
</style>