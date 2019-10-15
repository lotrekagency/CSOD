<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Aggiungi un messaggio</h1>
                <form @submit.prevent="onSubmit">
                  <textarea
                      v-model="message_body"
                      class="form-control"
                      placeholder="Scrivi qualcosa..."
                      rows="3">
                  </textarea>
                  <br>
                  <button
                    class="btn btn-success"
                    type="submit"
                    >Invio
                  </button>
                </form>
                <p class="muted error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
    name: "MessageEditor",

    data() {
      return{
        message_body: null,
        error: null
      }
    },

    methods: {
      onSubmit() {
        if (!this.message_body) {
            this.error = "Il campo non può essere vuoto!"
        } else if (this.message_body.length > 240) {
            this.error= "Non superare i 240 caratteri"
        } else {
          let endpoint = "/api/messagestext/";
          let method = "POST";
          apiService(endpoint, method, {content: this.message_body})
              .then(message_data => {
                  this.$router.push({
                      name: "message",
                      params: { slug: message_data.slug }
                  });
              });
        }
      }
    },
    created() {
      document.title="Message Editor - CSOD";
    }
}
</script>

<style lang="css" scoped>
</style>
