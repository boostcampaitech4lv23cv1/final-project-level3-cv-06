import { createApp } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import router from "./router";
import mixins from "./mixins";
import store from "./store/store";
import bgm from "./assets/BGM.mp3";
loadFonts();

// createApp(App).use(router)
//   .use(vuetify)
//   .mixin(mixins)
//   .mount('#app')

const app = createApp(App);
app.config.globalProperties.audio = new Audio(bgm);
app.use(router);
app.use(store);
app.use(vuetify, {});
app.mixin(mixins);
app.mount("#app");
