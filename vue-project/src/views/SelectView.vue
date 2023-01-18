<template>
    <v-app class=hero>
        <v-container height="100%">
            <v-row class="d-flex justify-center mt-10">
                <div :style="{ 'font-size': '30px', 'color': 'white' }" class="d-flex justify-center align-center">Save
                    Paint!</div>
            </v-row>
            <v-row class="mt-16">
                <v-col cols="6">
                    <v-card class="mx-auto mb-16" style="width: 150px;">
                        <v-card-title class="text-center">Mode</v-card-title>
                    </v-card>
                    <v-radio-group v-model="selectedMode" row>
                        <v-btn rounded v-for="item in modeItems" :key="item.value" :value="item.value" v-radio
                            @click="changeMode(item.value)"
                            :class="{ 'darken': selectedMode === item.value, 'mb-4 w-50 mx-auto grey': true, }">
                            {{ item.text }}
                        </v-btn>
                    </v-radio-group>
                </v-col>
                <v-col cols="6">
                    <v-card class="mx-auto mb-16" style="width: 150px;">
                        <v-card-title class="text-center">Category</v-card-title>
                    </v-card>
                    <v-radio-group v-model="selectedCategory" row>
                        <v-btn rounded v-for="item in categoryItems" :key="item.value" :value="item.value" v-radio
                            @click="changeCategory(item.value)"
                            :class="{ 'darken': selectedCategory === item.value, 'mb-4 w-50 mx-auto grey': true, }">
                            {{ item.text }}
                        </v-btn>
                    </v-radio-group>
                </v-col>
            </v-row>
            <v-col cols=12 class="d-flex justify-center mt-16">
                <v-btn :disabled="categoryIsEmpty" color="primary" @click="startGame">Game start</v-btn>
            </v-col>
        </v-container>


    </v-app>
</template>

<script>
export default {
    data() {
        return {
            categoryItems: [
                { text: 'Random', value: 'Raondom' },
                { text: 'Actors', value: 'Actors' },
                { text: 'Movie Posters', value: 'Movie Posters' },
                { text: 'Animals', value: 'Animals' },
                { text: 'Landmarks', value: 'Landmarks' },
                { text: 'Masterpieces', value: 'Masterpieces' },
            ],
            selectedCategory: '',
            selectedMode: '',
            modeItems: [
                { text: 'Paint Transformer', value: 'Paint Transformer' },
                { text: 'Oil Transformer', value: 'Oil Transformer' },
            ],
        }
    },
    computed: {
        categoryIsEmpty() {
            return this.selectedCategory === '' || this.selectedMode === '';
        }
    },
    methods: {
        startGame() {
            this.$router.push({ path: '/test', query: { category: this.selectedCategory, mode: this.selectedMode } })
        },
        changeMode(value) {
            this.selectedMode = value
        },
        changeCategory(value) {
            this.selectedCategory = value
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

.darken {
    filter: brightness(80%);
}

.grey {
    background-color: #9E9E9E;
    color: #fff;
}
</style>