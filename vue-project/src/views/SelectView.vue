<template>
    <v-card class="mx-auto" style="width: 300px;">
        <v-card-title class="text-center">Save Paint!</v-card-title>
    </v-card>
    <v-container fluid>
        <v-row>
            <v-col
            cols="12"
            sm="6"
            md="6">
            <v-card class="mx-auto" style="width: 300px;">
            <v-card-title class="text-center">Select Mode</v-card-title>
            </v-card>
            <v-radio-group v-model="selected_mode">
            <v-radio v-for="option in selectmode" :label="option" :key="option" :value="option"></v-radio>
            </v-radio-group>
            </v-col>
            <v-col
            cols="12"
            sm="6"
            md="6">
            <v-card class="mx-auto" style="width: 300px;">
            <v-card-title class="text-center">Select Category</v-card-title>
            </v-card>
            <v-radio-group v-model="selected_category">
            <v-radio v-for="option in selectcategory" :label="option" :key="option" :value="option"></v-radio>
            </v-radio-group>
            </v-col>
        </v-row>
</v-container>

<v-btn color="primary" @click="startGame">Game start</v-btn>
</template>

<script>
export default{
    data(){ 
        return{
            selectmode:['Paint Transformer','Oil Transformer'],
            selected_mode:'',
            selectcategory:['ALL','ANIMAL','CELEBRITY','LANDMARK','ART'],
            selected_category:'',
        }
    },
    methods: {
    startGame() {
      this.$router.push({path:'/game'})
    }
  }
}
</script>