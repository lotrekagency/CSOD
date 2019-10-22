<!-- Questo è il nostro route component, che è di fatto un componente di tipo
single-file -->
<template>
  <div id="app">
      <SidebarComponent />
      <router-view />
  </div>
</template>

<script>
import SidebarComponent from "./components/Sidebar.vue"

export default {
  name: "App",
  components: {
      SidebarComponent
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
