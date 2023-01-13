<template>
    <v-card class="mx-auto" style="width: 300px;">
        <v-card-title class="text-center">Save Paint!</v-card-title>
    </v-card>
    <v-btn @click='start'></v-btn>
    <img :src="'data:image/gif;base64,'+test" alt="gif"/>


</template>

<script>
    export default{
        data(){
            return {
                test:0
            };
        },
        methods:{
            async getList(){
               let response = await this.$api('http://127.0.0.1:8000','POST',{category:'animal'})
               return response
            },
            start() {
            this.getList()
            .then((response) => {
            this.test = response;
            this.test=response['image'];
            });
        }
    }

    }
</script>