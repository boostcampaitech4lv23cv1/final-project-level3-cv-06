<template>
    {{answer}}
</template>

<script>
    export default{
        data(){
            return{
            origin_img:this.$store.state.origin_img,
            paint_img:this.$store.state.paint_img,
            answer:this.$store.state.answer
            }
        }
    }
</script>