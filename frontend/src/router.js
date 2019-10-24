// utilizzaimo vue router per specificare i percorsi che andranno a formare
// la nostra applicazione
import Vue from "vue";
import Router from "vue-router";
import AnswerEditor from "./views/AnswerEditor.vue";
import Home from "./views/Home.vue";
import Welcome from "./views/Welcome.vue";
import Message from "./views/Message.vue";
import MessageEditor from "./views/MessageEditor.vue";
import NotFound from "./views/NotFound.vue";

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
      path: "/write/:slug?",   // ? il punto interrogativo serve per indicare che un parametro è opzionale
      name: "message-editor",
      component: MessageEditor,
      props: true
    },
    {
      path: "/answer/:id",
      name: "answer-editor",
      component: AnswerEditor,
      props: true
    },
    {
      path: "*",
      name: "page-nou-found",
      component: NotFound
    },
  ]
});
