<template>
  <sidebar-menu :menu="menu" />
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
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

      </div>  <!--container -->
  </nav>
</template>

<script>
    export default {
        data() {
            return {
                menu: [
                    {
                        header: true,
                        title: 'Main Navigation',
                        hiddenOnCollapse: true
                    },
                    {
                        href: '/',
                        title: 'Dashboard',
                        icon: 'fa fa-user'
                    },
                    {
                        href: '/charts',
                        title: 'Charts',
                        icon: 'fa fa-chart-area',
                        child: [
                            {
                                href: '/charts/sublink',
                                title: 'Sub Link'
                            }
                        ]
                    }
                ]
            }
        }
    }
</script>

<style scoped>
props: {
    // Sidebar menu (required)
    menu: {
      type: Array,
      required: true
    },

    // Sidebar Collapse state
    collapsed: {
      type: Boolean,
      default: false
    },

    // Sidebar width (expanded)
    width: {
      type: String,
      default: '350px'
    },

    // Sidebar width (collapsed)
    widthCollapsed: {
      type: String,
      default: '50px'
    },

    // Keep only one child opened at a time (first level only)
    showOneChild: {
      type: Boolean,
      default: false
    },

    // Keep all child open
    showChild: {
      type: Boolean,
      default: false
    },

    // Sidebar right to left
    rtl: {
      type: Boolean,
      default: false
    },

    // Make sidebar relative to the parent (by default the sidebar is relative to the viewport)
    relative: {
      type: Boolean,
      default: false
    },

    // Hide toggle collapse btn
    hideToggle: {
      type: Boolean,
      default: false
    },

    // Sidebar theme (available themes: 'white-theme')
    theme: {
      type: String,
      default: ''
    },

    // Disable hover on collapse mode
    disableHover: {
      type: Boolean,
      default: false
    }
}
</style>
