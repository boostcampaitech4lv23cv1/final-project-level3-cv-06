<template>
  <mainview :page="$route.query.page" />
</template>
<script>
import mainview from "../components/ExampleView.vue";

export default {
  components: {
    mainview,
  },
  data() {
    return {};
  },
};
</script>
