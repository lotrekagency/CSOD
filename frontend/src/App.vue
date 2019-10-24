<!-- Questo è il nostro route component, che è di fatto un componente di tipo
single-file -->
<template>
  <div id="app">
      <SidebarComponent />
      <router-view />
  </div>
</template>

<script>
import { apiService } from "./common/api.service";
import SidebarComponent from "./components/Sidebar.vue"

export default {
  name: "App",
  components: {
      SidebarComponent
  },
  data(){
    return {
      userUsername: null
    }
  },
  methods: { /* stiamo settando lo user in local storage e così possiamo accedere al nome utente dello user connesso */
    async setUserInfo() {
      await apiService("/api/user/")  /* questo endpoint lo trovo nel file users/api/urls.py (current-user) */
              .then(result => {
                  this.userUsername = result.username;
                  window.localStorage.setItem("username", this.userUsername);
              })
    }
  },
  created() {
      this.setUserInfo();
  }
}
</script>


<style>
body {
  font-family: "Playfair Display", serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>
