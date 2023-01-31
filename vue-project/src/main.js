import { createApp } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import router from "./router";
import mixins from "./mixins";
import myIcon from "./myIcon";
import store from "./store/store";

loadFonts();

// createApp(App).use(router)
//   .use(vuetify)
//   .mixin(mixins)
//   .mount('#app')

const app = createApp(App);
app.config.globalProperties.audio = new Audio(
  "https://cdn.pixabay.com/download/audio/2021/07/28/audio_81a4a9bc2a.mp3?filename=bossa-nova-piano-instrumental-brasil-5732.mp3"
);
app.use(router);
app.use(store);
app.use(vuetify, {
  icons: {
    "my-icon": myIcon,
  },
});
app.mixin(mixins);
app.mount("#app");
