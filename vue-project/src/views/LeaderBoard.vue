<template>
    <v-app class="hero">
        <v-row class="d-flex justify-center">
            <ranking :style="{ height: '15vh', margin: '10vh 0vw 0vh 0vw' }" />
        </v-row>
        <v-row class="d-flex justify-center">
            <v-col cols=4>
                <v-table class="table">
                    <thead>
                        <tr>
                            <th class="text-center">
                                Name
                            </th>
                            <th class="text-center">
                                Score
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in ranking" :key="item.name">
                            <td class="text-center">{{ item.name }}</td>
                            <td class="text-center">{{ item.score }}</td>
                        </tr>
                    </tbody>
                </v-table>
            </v-col>
        </v-row>
    </v-app>
</template>

<script>
import ranking from '../svg/rankingText.vue'

export default {
    components: {
        ranking
    },
    data() {
        return {
            ranking: [
                { name: 'a', score: '1' },
                { name: 'b', score: '2' },
                { name: 'c', score: '3' },
                { name: 'd', score: '4' },
                { name: 'e', score: '5' },
                { name: 'f', score: '6' },
                { name: 'g', score: '7' },
                { name: 'h', score: '8' },
                { name: 'i', score: '9' },
                { name: 'j', score: '10' }

            ]
        }
    },


}
</script>

<style>
.hero {
    background: url("../assets/test.jpg");
    background-size: cover;
}

.table {
    background-color: transparent;
}
</style>