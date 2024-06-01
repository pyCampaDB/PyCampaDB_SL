<template>
  <div class="container">
    <!-- navbar -->
    <navbar-component v-if="$route.path==='/about' || $route.path==='/'" />
    <navigation-component v-if="$route.path==='/about'"/>
    <home-component v-if="$route.path==='/'" />
    <router-view/>
    <footer-component/>
  </div>
</template>

<script setup>
import FooterComponent from './components/FooterComponent.vue'
import NavigationComponent from './components/NavigationComponent.vue'
import NavbarComponent from './components/NavbarComponent.vue'
import HomeComponent from './components/HomeComponent.vue'
/*export default{
  name: 'App',
  components: {
    FooterComponent,
    NavbarComponent,
    NavigationComponent
  }
}*/
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
