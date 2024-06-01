<template>
<section class="mt-5 text-center mx-auto">
      <h1 class="text-danger">pyCampaDB Security</h1>
      <div class="mt-3" v-if="$route.path !== '/about'">
        <button type="button" class="btn btn-warning" v-for="service in services" :key="service.title" 
      @click="getTitle(service.title)">{{service.title}}</button>
        <!--<router-link class="nav-link active" aria-current="page" :to="`/services/${service.title}`">{{service.title}}</router-link>-->  
      </div>
      <hr>
    </section>
</template>
  <script setup>
  import axios from 'axios';
  import {ref, defineEmits, onMounted} from 'vue';
  
  const services = ref([])
  const serviceReceived=ref(null)
  const emit = defineEmits(['getTitle'])
  
  const getTitle = (service)=>{
    emit('getTitle', service);
  }
  
  onMounted (()=>{
    axios.get('http://127.0.0.1:8000/api/services/').then(
      response => {
            services.value=response.data
          }
        ).catch(e => {console.log(e)})
      })
  </script>
  
  <style>
  button {
    margin-right: 5px;
  }
  
  button + button, button:first-child {
    margin-left: 5px;
  }
  
  @media (max-width: 768px){
    button {
      width: 100%;
      margin: 0 0 5px !important;
      box-sizing: border-box;
    }
  }
  </style>
  