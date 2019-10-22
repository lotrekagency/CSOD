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
                  <!-- <form enctype="multipart/form-data">
                      <input type="type" name="file" v-on:change="fileChange($event.target.files)">
                      <input type="type" name="file" v-on:change="fileChange($event.target.files)">
                      <button type="button" v-on:click="upload()">Upload</button>
                  </form> -->
                  <!-- <label class="select-file"> -->
                    <input type="file" @change="onFileChanged">
                    <button
                    class="btn btn-success"
                    type="submit" @click="onUpload">Upload!</button>
                  <p class="muted error mt-2">{{ error }}</p>
                    <!-- <input type="type" name="file" @change="fileChange($event, index)"> -->
                  <!-- </label> -->
                </form>
                  <br>
                  <!-- <button
                    class="btn btn-success"
                    type="submit"
                    >Invio
                  </button> -->


            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import axios from "axios";
export default {
    name: "MessageEditor",

    data() {
      return{
        message_body: null,
        error: null,
        selectedFile: null
        //files: new FormData()
        // message_cover: '',
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
          apiService(endpoint, method, {content: this.message_body, cover: this.message_cover})
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
