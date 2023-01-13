<template>
    <v-container>
        <v-row>
            <v-col cols=12><v-spacer></v-spacer></v-col>
            <v-col cols=12><v-spacer></v-spacer></v-col>
        </v-row>
        <v-row class="justify-center">
            <div :style="{ 'font-size': '30px', 'color': 'white' }" >4/9</div>
        </v-row>
        <v-row>
            <v-col cols=12><v-spacer></v-spacer></v-col>
            <v-col cols=12><v-spacer></v-spacer></v-col>
            <v-col cols=12><v-spacer></v-spacer></v-col>
        </v-row>
        <v-row>
        <v-img src="../assets/example.jpg" height="250" width="250"/>
        </v-row>

    </v-container>  


</template>

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