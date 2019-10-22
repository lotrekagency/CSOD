<template lang="html">
  <nav id="sidebar">
    <div class="wrapper">
      <div class="sidebar-header">
        <router-link
          :to="{ name: 'welcome'}"
          class="sidebar-brand"
          >CSOD
        </router-link>
        <div id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link
                :to="{ name: 'home'}"
                class="btn btn-sm btn-info"
                >Messaggi
              </router-link>
            </li>

            <li class="nav-item ">
              <router-link
                :to="{ name: 'message-editor'}"
                class="btn btn-sm btn-primary"
                >Aggiungi messaggio
              </router-link>
            </li>

            <li class="nav-item">
              <a class="btn btn-sm btn-secondary"
                 href="/accounts/logout/"
                 >Logout
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div id="content">
      <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
          <button type="button" id="sidebarCollapse" class="btn btn-info">
            <i class="fas fa-align-left"></i>
            <span>Toggle Sidebar</span>
          </button>
        </div>
      </nav>
    </div>
  </nav>

    <!-- Page Content -->
  <!-- <div id="content">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <button type="button" id="sidebarCollapse" class="btn btn-info">
          <i class="fas fa-align-left"></i>
          <span>Toggle Sidebar</span>
        </button>
      </div>
    </nav>
  </div> -->

</template>

<script>
export default {
  name: "SidebarComponent",
}

// $(document).ready(function () {
//
//   $('#sidebarCollapse').on('click', function(){
//     $('#sidebar').toggleClass('active');
//   });
// });

</script>

<style lang="css" scoped>
@import "https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700";
.wrapper {
    display: flex;
    align-items: flex-start;
}

#sidebar {
    min-width: 250px;
    max-width: 250px;
    min-height: 100vh;
    position: relative;
    float: left;
}

#sidebar.active {
    margin-left: -250px;
}

a[data-toggle="collapse"] {
    position: relative;
}

.dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}

@media (max-width: 768px) {
    #sidebar {
        margin-left: -250px;
    }
    #sidebar.active {
        margin-left: 0;
    }
}

body {
    font-family: 'Poppins', sans-serif;
    background: #fafafa;
}

p {
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
}

a, a:hover, a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}

#sidebar {
    /* don't forget to add all the previously mentioned styles here too */
    background: #2595ab;
    color: #fff;
    transition: all 0.3s;
}

#sidebar .sidebar-header {
    padding: 20px;
    background: #2595ab;
    text-align: center;
}

#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #47748b;
}

#sidebar ul p {
    color: #fff;
    padding: 10px;
}

#sidebar ul li a {
    padding: 10px;
    font-size: 1.1em;
    display: block;
}
#sidebar ul li a:hover {
    color: #7386D5;
    background: #fff;
}

#sidebar ul li.active > a, a[aria-expanded="true"] {
    color: #fff;
    background: #6d7fcc;
}
ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #6d7fcc;
}

</style>
