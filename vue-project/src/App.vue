<template>
  <v-app>
    <v-main>
      <router-view />
      <K-progress />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
};
</script>
