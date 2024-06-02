<template>
    <nav class="navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="collapse-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <router-link class="nav-link active" aria-current="page" to="/" style="margin-right: 15px;height: 15px;"> Inicio </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" aria-current="page" to="/products" style="margin-right: 15px;height: 15px;"> Productos </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link active" aria-current="page" to="/services" style="margin-right: 15px;height: 15px;"> Servicios </router-link>
            </li>
            
            <li class="nav-item">
                <router-link class="nav-link active" aria-current="page" to="/assets" v-if="isAuthenticated" style="margin-right: 15px;height: 15px;"> Videos </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" aria-current="page" to="/sales" v-if="isAuthenticated" style="height: 15px;"> Compras </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/about" style="margin-right: 15px;height: 15px;"> Acerca de nosotros  </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link active" aria-current="page" to="/register" v-if="!isAuthenticated" style="margin-right: 15px;height: 15px;"> Registrarse </router-link>
            </li>
          </ul>
          <div class="auth-actions" style="margin-right: 10px;">
            <span v-if="isAuthenticated">Bienvenido, {{ username.username }}</span>
            <button v-if="isAuthenticated" @click="handleLogout" class="btn btn-outline-danger ms-2">Cerrar Sesión</button>
            <router-link v-else class="btn btn-outline-primary ms-2" to="/login">Iniciar Sesión</router-link>
          </div>
          <form class="d-flex" role="search" @submit.prevent="submitForm"><!--submit.prevent sirve para que no recargue la pág cuando pulsas el buscador-->
            <input class="form-control me-2" type="search" placeholder="Buscar..." aria-label="Search" v-model="searchText">
              <button class="btn btn-outline-success" type="submit" @click="getSearch">Buscar</button>
          </form>
          
        </div>
      </div>
    </nav>
</template>
<script setup>
    import {ref,defineEmits,computed} from 'vue';
    import { isAuthenticated, username, logout } from '@/auth';
   const searchText=ref('')
   const searchService=ref('')
   const emitSearch = defineEmits(['getSearchText', 'getSearchService','getSearchAssets'])
   const getSearch = ()=>{
    if (window.location.pathname==='/products'){
      emitSearch('getSearchText', searchText.value)
    } else if (window.location.pathname==='/services'){
      emitSearch('getSearchService', searchText.value)
    } else if (window.location.pathname==='/assets'){
      emitSearch('getSearchAssets', searchText.value)
    }
    
   }
   const getSearchService = ()=>{
    emitSearch('getSearchService', searchService.value)
   }
   const getSearchAssets = ()=>{
    emitSearch('getSerachAssets', searchAsset.value)
   }
   const handleLogout = () => {
      logout();  // Llamar a la función logout
      // Redirigir a la página de inicio de sesión después de cerrar sesión
       window.location.href = '/login';
    };
    const authenticated=computed(()=>isAuthenticated.value);
    const user=computed(()=>username.value);
</script>
<style scoped>
.auth-actions {
  display: flex;
  align-items: center;
}
</style>