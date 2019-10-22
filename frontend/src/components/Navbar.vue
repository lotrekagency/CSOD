<template lang="html">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark my-navbar">
    <div class="container">
      <router-link
        :to="{ name: 'welcome'}"
        class="navbar-brand"
        >CSOD
      </router-link>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link
              :to="{ name: 'home'}"
              class="btn btn-sm btn-success"
              >Messaggi
            </router-link>
          </li>

          <li class="nav-item mx-1">
            <router-link
              :to="{ name: 'message-editor'}"
              class="btn btn-sm btn-danger"
              >Aggiungi messaggio
            </router-link>
          </li>

          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary"
               href="/accounts/logout/"
               >Logout
            </a>
          </li>
        </ul>
      </div>

    </div>  <!--container-->
</nav>
</template>

<script>
export default {
name: "NavbarComponent"
}
</script>

<style lang="css">

.my-navbar {
  border-bottom: 1px solid #DDD;
}

.navbar-brand {
font-weight: bold;
font-size: 130%;
}
.navbar-brand:hover {
color: #DC3545 !important;
}
</style>
