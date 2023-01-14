<template>
  <v-app class="hero">
    <v-container class="h-25" text-color="white">
        <div :style="{ 'font-size': '30px', 'color': 'white' }" class="d-flex justify-center align-center">Save Paint!</div>
    </v-container>  
    <v-btn
        class="ma-2"
        variant="text"
        v-bind="{icon:sound_icon}"
        color="white"
        style="position: absolute; left: 1200px; top: 50px "
        @click="soundChange"
      ></v-btn>
    <v-btn
        class="ma-2"
        variant="text"
        icon="mdi-file-document"
        color="white"
        style="position: absolute; left: 1200px; top: 85px "
        @click='movePage("/description",{page:1})'
      ></v-btn>


    <v-container style="position: relative; top: 350px;">
      <v-row class="d-flex justify-center align-center mb-6">
        <v-btn variant="flat" color="red" width="15%" @click='movePage("/select")'>
          Game Start
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center aligncenter">
        <v-btn variant="flat" color="yellow" width="15%" class="text-white" @click='movePage("/transform")'>
          Paint My Image
        </v-btn>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  export default {
    data(){
              return {
                  absolute: true,
                  overlay: false,
                  sound_icon:"mdi-volume-high",
                  current_page:'page1'
              };
          },
    methods: {
      movePage(route) {
        this.$router.push({path:route,
                            query:{'page':1}
                          })
        },
      soundChange(){
          if (this.sound_icon=='mdi-volume-high'){
            this.sound_icon='mdi-volume-off'
          }
          else{
            this.sound_icon='mdi-volume-high'
          }

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
</style>