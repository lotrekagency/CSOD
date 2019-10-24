<template lang="html">
  <div class="message-actions">
    <router-link
      :to="{ name: 'message-editor', params: { slug: slug } }"
      class="btn btn-sm btn-outline-secondary mr-1"
      ><span>Modifica</span>
    </router-link>

    <button
      class="btn btn-sm btn-outline-danger"
      @click="deleteMessage"
      >Cancella
    </button>

  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MessageActions",

  props: {
    slug: {
      type: String,
      required: true
    }
  },

  methods: {
    async deleteMessage() {
      let endpoint = `/api/messagestext/${this.slug}/`;
      try {
          await apiService(endpoint, "DELETE");
          this.$router.push("/home");
      } catch (err) {
          console.log(err);
      }
    }
  }
}
</script>

<style lang="css" scoped>
</style>
