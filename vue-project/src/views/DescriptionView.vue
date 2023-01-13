<template>
    <!-- <v-app class="hero">
        <v-overlay v-model="overlay" contained class="align-center justify-center">
            <v-container class="no-overlay-container">
              123
            </v-container>
            <v-container class="overay-container">
              123
            </v-container>
        </v-overlay>
    </v-app> -->
    <v-app class="hero">
        <v-overlay v-model="overlay" class="justify-center">
            <mainview></mainview>
        </v-overlay>
    </v-app>
</template>
<script>
    import mainview from '../components/ExampleView.vue'

    export default {
        components:{
            mainview
        },
        data(){
                return {
                    overlay: true,
                };
            },
    }

</script>


<style scoped>
.hero {
  background: url('../assets/back.jpg');
  background-size: cover;
  height: 100vh;
}
.no-overlay-container {
  position: relative;
  z-index: 1;
  background-color: blue;
}
.overlay-container {
    background-color: blue;
}
</style>