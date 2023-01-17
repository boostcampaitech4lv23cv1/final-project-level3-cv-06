<template>
    <F class="icon"></F>
</template>

<script>
import F from '../assets/F.svg'
export default {
    components: {
        F
    },
    data() {
        return {
            rank: this.$store.state.rank
        };
    },
}
</script>