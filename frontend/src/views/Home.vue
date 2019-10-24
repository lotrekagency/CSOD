<template>
  <div class="home-view">
    <div class="container">
        <div class="mt-2">
            <div v-for="message in messages"
               :key="message.pk">

              <p class="mb-0">Messaggio aggiunto da
                <span class="author_name">{{ message.author }}</span>
              </p>
              <h2>
                <router-link
                  :to="{ name: 'message', params: {slug: message.slug, pk: message.pk} }"
                  class="message-link">
                  {{ message.content }}
                </router-link>
              </h2>
              <p>Risposte: {{ message.answers_count }}</p>
              <hr>
            </div>

        </div>
        <div class="my-4">
            <p v-show="loadingMessages">...loading...</p>
          <button
             v-show="next"
             @click="getMessages"
             class="btn btn-sm btn-outline-success"
             >Carica Ancora
          </button>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "../common/api.service.js";
export default {
  name: "home",

  data() {
    return {
      messages: [],
      next: null,
      loadingMessages: false
    }
  },

  methods: {
    getMessages() {
      let endpoint = "api/messagestext/";
      if (this.next) {
          endpoint = this.next;
      }
      this.loadingMessages = true;
      apiService(endpoint)
        .then(data => {
            this.messages.push(...data.results);
            this.loadingMessages = false;
            if(data.next) {
                this.next = data.next;
            } else {
              this.next = null;
            }
        })
    }
  },

  created() {
    this.getMessages();
    document.title= "Messaggi";
  }
};
</script>

<style media="screen">
  .author_name {
    font-weight:  bold;
    color: #DC3545;
  }

  .message-link {
    font-weight:  bold;
    color: black;
  }

  .message-link:hover {
    color: #343A40;
    text-decoration: none;
  }

</style>
