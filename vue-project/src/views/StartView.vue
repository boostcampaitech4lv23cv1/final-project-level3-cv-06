<template>
  <v-app class="hero">
    <v-container class="mt-16" text-color="white">
        <div :style="{ 'font-size': '30px', 'color': 'white' }" class="d-flex justify-center align-center">Save Paint!</div>
    <v-row class="d-flex justify-end mt-10">
      <v-btn
          variant="text"
          v-bind="{icon:sound_icon}"
          color="white"
          @click="soundChange"
        ></v-btn>
    </v-row>
    <v-row class="d-flex justify-end">
      <v-btn
          variant="text"
          icon="mdi-file-document"
          color="white"
          @click='movePage("/description",{page:1})'
        ></v-btn>
    </v-row>

      <v-row class="d-flex justify-center align-center buttons">
        <v-btn variant="flat" color="red" width="15%" @click='movePage("/select")'>
          Game Start
        </v-btn>
      </v-row>
      <v-row class="d-flex justify-center aligncenter mt-6">
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
      movePage(route,query) {
        this.$router.push({path:route,
                            query:query
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

.buttons {
  margin-top:400px
}
</style>