import Vue from "vue";
import App from "./App.vue";
import router from "./router";



Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");

// il file main.js è il file principale che va a renderizzare il nostro
// componente "#app" e lo monta nel DOM. Abbiamo la creazione di una nuova istanza
// di Vue e stiamo andare a montare "#app" al interno di una div con id #app.
