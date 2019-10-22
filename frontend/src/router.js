// utilizzaimo vue router per specificare i percorsi che andranno a formare
// la nostra applicazione
import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Welcome from "./views/Welcome.vue";
import Message from "./views/Message.vue";
import MessageEditor from "./views/MessageEditor.vue";


Vue.use(Router);

export default new Router({
  mode: "history",
  //base: process.env.BASE_URL,  commento cosi nell url non mi compare http:/0.0.0.0:8080
  routes: [
    {
      path: "/",
      name: "welcome",
      component: Welcome,
    },
    {
      path: "/home",
      name: "home",
      component: Home,
    },

    {
      path: "/message/:slug",
      name: "message",
      component: Message,
      props: true
    },
    {
      path: "/write",
      name: "message-editor",
      component: MessageEditor,
    }
  ]
});
