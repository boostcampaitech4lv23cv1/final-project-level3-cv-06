<template>
    <mainview :page="$route.query.page"/>
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