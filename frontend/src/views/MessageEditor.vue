<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Aggiungi un messaggio</h1>
                <form @submit.prevent="onSubmit">
                  <textarea
                      v-model="messageBody"
                      class="form-control"
                      placeholder="Scrivi qualcosa..."
                      rows="3">
                  </textarea>
                  <!-- <label class="select-file"> -->
                    <input type="file" @change="onFileChanged">
                    <button
                    class="btn btn-success"
                    type="submit" @click="onUpload">Invio</button>
                  <p class="muted error mt-2">{{ error }}</p>
                    <!-- <input type="type" name="file" @change="fileChange($event, index)">
                  </label> -->
                </form>
                <br>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import axios from "axios";
export default {
    name: "MessageEditor",

    props: {
        slug: {
          type: String,
          required: false    // false perchè usiamo questo componente per modificare le domande
        },                   // ma lo stiamo già utilizzando di crearne di nuove
        previousMessage:{
          type: String,
          required: false
        }
    },

    data() {
      return{
        messageBody: this.previousMessage || null,
        error: null,
        // selectedFile: null
        //files: new FormData()
        // message_cover: '',
      }
    },

    async beforeRouteEnter(to, from, next) {
      if (to.params.slug !== undefined) {
        let endpoint = `/api/messagestext/${to.params.slug}/`;
        await apiService(endpoint)
                .then((data) => {
                  to.params.previousMessage = data.content;
                })
      }
      return next();
    },

    methods: {
      onSubmit() {
        if (!this.messageBody) {
            this.error = "Il campo non può essere vuoto!"
        } else if (this.messageBody.length > 240) {
            this.error= "Non superare i 240 caratteri"
        } else {
          let endpoint = `/api/messagestext/`;
          let method = "POST";
          if (this.previousMessage) {
            method = "PUT";
            endpoint += `${this.slug}/`;
          }
          apiService(endpoint, method, {content: this.messageBody, cover: this.message_cover})
              .then(message_data => {
                  this.$router.push({
                      name: "message",
                      params: { slug: message_data.slug }
                  });
              });
        }
      },
      onFileChanged(event) {
        this.selectedFile = event.target.files[0]
      },
      onUpload() {
        const formData = new FormData()
        formData.append('myFile', this.selectedFile, this.selectedFile.name)
        axios.post('http://localhost:8000/messagestext/messagetext/', formData)
      }
    },
      created() {
        document.title="Message Editor - CSOD";
      }
  };

</script>

<style lang="css" scoped>
.submit-file{
  visibility: hidden;
}
</style>
