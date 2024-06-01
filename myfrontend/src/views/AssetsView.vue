<template>
    <navbar-component @getSearchAssets="search"/>
    <assets-component />
    <div class="mb-3" v-if="searchTextRule">
    <h3>Videos con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los videos</button>
  <div class="alert alert-warning" role="alert" v-if="filteredassets.length===0">De <strong>{{searchTextRule}}</strong> me quedao a cero pisha</div>
  </div>
  <div class="mb-3" v-if="videoReceived">
    <h3>Videos de <strong>{{ videoReceived }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los videos</button>
  <div class="alert alert-warning" role="alert" v-if="filteredassets.length===0">De <strong>{{videoReceived}}</strong> me quedao a cero pisha</div>
  </div>
      <div>
      <div class="row row-cols-1 row-cols-md-3 g-4 justify-content-center">
          <div class="col" v-for="asset in filteredassets" :key="asset.title">
            <div class="card text-center mx-auto">
              <div class="card-body">
                <h5 class="card-video">Video {{asset.title}}</h5>
                <video width="100%" controls>
                <source :src="asset.video" type="video/mp4">
                Your browser does not support the video tag.
                </video>
                <p>Video: {{ getFileName(asset.video) }}</p>
              </div>
          </div>
        </div>
      </div>
    </div>
    
  </template>
  <script setup>
  import axios from 'axios';
  import NavbarComponent from '@/components/NavbarComponent.vue';
  import assetsComponent from '@/components/AssetsComponent.vue';
  import {ref ,onMounted} from 'vue'
  import { isAuthenticated, username } from '@/auth';

  const getFileName = (path) => {
    // Dividir la cadena en partes usando '/' como separador
    const parts = path.split('/');
    // Tomar el último elemento del array resultante
    const fileName = parts[parts.length - 1];
    const filenamewithend = fileName.split('.')
    const filename = filenamewithend[0]
    return filename;
  }
  const assets = ref([])
  const filteredassets=ref([]);
  const videoReceived=ref(null);
  const searchTextRule=ref(null)

const search = (searchText)=>{
  videoReceived.value=null
  searchTextRule.value=searchText
  if(searchText) {
    filteredassets.value=assets.value.filter((asset)=>{
      return asset.title === parseInt(searchText);
    })
  } else {
    filteredassets.value=assets.value
  }
}
  //[*]

  const resetFilter = () => {
  videoReceived.value =null
  searchTextRule.value=null
  filteredassets.value=assets.value
}

onMounted(() => {
  const token = localStorage.getItem('access_token'); // Obtenemos el token de autenticación desde localStorage
  if (token) { // Si hay un token presente, hacemos la solicitud
    axios.get('http://localhost:8000/api/assets/', {
      headers: {
        Authorization: `Bearer ${token}` // Enviamos el token en el encabezado Authorization
      }
    }).then(response => {
      assets.value = response.data;
      filteredassets.value = assets.value;
    }).catch(e => {
      if (e.response && e.response.status === 401) {
        console.error('Unauthorized. Please check the token.');
        // Redirigir al login si el token es inválido o ha expirado
        window.location.href = '/login';
      } else {
        console.log(e);
      }
    });
  } else {
    console.log("User is not authenticated");
    // Redirigir al login si no hay token
    window.location.href = '/login';
  }
});




  /*onMounted (()=>{
     // Si hay un token presente, hacemos la solicitud
     const token = localStorage.getItem('access_token'); // Obtenemos el token de autenticación desde localStorage
  if (token) { // Si hay un token presente, hacemos la solicitud
    axios.get('http://localhost:8000/api/assets/', {
      headers: {
        Authorization: `Token ${token}` // Enviamos el token en el encabezado Authorization
      }
    }).then(response => {
      assets.value = response.data;
      filteredassets.value = assets.value;
    }).catch(e => {
      console.log(e);
    });
  } else {
    console.log("User is not authenticated");
  }
});*/
      /*axios.get('http://localhost:8000/api/assets/').then(
        response => {
            assets.value=response.data
            filteredassets.value=assets.value
          }
        ).catch(e => {console.log(e)})
      })*/


    
      </script>


  
  