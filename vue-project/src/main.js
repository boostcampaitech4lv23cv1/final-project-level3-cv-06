import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import mixins from './mixins'

loadFonts()

// createApp(App).use(router)
//   .use(vuetify)
//   .mixin(mixins)
//   .mount('#app')

const app = createApp(App)
app.use(router)
app.use(vuetify)
app.mixin(mixins);
app.mount('#app')