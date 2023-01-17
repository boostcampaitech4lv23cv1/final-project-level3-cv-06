<template>
    {{ rank }}
</template>

<script>
export default {
    data() {
        return {
            rank: this.$store.state.rank
        };
    },
}
</script>