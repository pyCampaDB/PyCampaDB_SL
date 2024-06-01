<template>
    <navbar-component @getSearchService="search"/>
    <services-component @getTitle="title"/>
    <div class="mb-3" v-if="searchTextRule">
    <h3>Servicios con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los servicios</button>
  <div class="alert alert-warning" role="alert" v-if="filteredServices.length===0">De <strong>{{searchTextRule}}</strong> me quedao a cero pisha</div>
  </div>
  <div class="mb-3" v-if="titleReceived">
    <h3>Productos de <strong>{{ titleReceived }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los servicios</button>
  <div class="alert alert-warning" role="alert" v-if="filteredServices.length===0">De <strong>{{titleReceived}}</strong> me quedao a cero pisha</div>
  </div>
      <div>
      <div class="row row-cols-1 row-cols-md-3 g-4 justify-content-center">
          <div class="col" v-for="service in filteredServices" :key="service.title">
            <div class="card text-center mx-auto">
              <div class="card-body">
                <img :src="service.image" class="card-img-top" alt="Imagen de {{ service.title }}">
                <h5 class="card-title">{{service.title}}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">{{service.title}}</h6>
                <p class="card-text">{{service.description}}</p>
              </div>
              <div class="card-footer text-danger">{{service.price}} {{ service.currency_types }}</div>
          </div>
        </div>
      </div>
    </div>
    <br><br>
    <p>Para solicitar un servicio, contacta con nosotros: <strong>py@campa.db</strong></p>
    
  </template>
  <script setup>
  import axios from 'axios';
  import NavbarComponent from '@/components/NavbarComponent.vue';
  import ServicesComponent from '@/components/ServicesComponent.vue';
  import {ref ,onMounted} from 'vue'
    
  const services = ref([])
  const filteredServices=ref([]);
  const titleReceived=ref(null);
  const searchTextRule=ref(null)

const search = (searchText)=>{
  titleReceived.value=null
  searchTextRule.value=searchText
  if(searchText) {
    filteredServices.value=services.value.filter((service)=>{
      const serviceTitle = service.title.toLowerCase();
      const searchTerm = searchText.toLowerCase();
      return serviceTitle.includes(searchTerm)
    })
  } else {
    filteredServices.value=services.value
  }
}
  /*const emit = defineEmits(['getService'])*/
  const title = (title)=>{
    searchTextRule.value=null
    titleReceived.value=title
    if(title) {
      filteredServices.value=services.value.filter((service)=>service.title === title )
    } else {
      filteredServices.value=services.value
    }
  }

  const resetFilter = () => {
  titleReceived.value =null
  searchTextRule.value=null
  filteredServices.value=services.value
}
  onMounted (()=>{
    axios.get('http://127.0.0.1:8000/api/services/').then(
      response => {
            services.value=response.data
            filteredServices.value=services.value
          }
        ).catch(e => {console.log(e)})
      })
      </script>
  
  