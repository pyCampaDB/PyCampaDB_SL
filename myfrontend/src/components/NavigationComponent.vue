<template>
  <section class="mt-5 text-center mx-auto">
    <h1 class="text-danger">pyCampaDB Security</h1>
    <!--<img class="img-fluid" :src="require('@/assets/img/camera.png')" alt=" " width="200" height="300">-->
    <div class="mt-3" v-if="$route.path !== '/about'">
      <button type="button" class="btn btn-warning" v-for="kind in kinds" :key="kind.kind" 
      @click="getKind(kind.kind)">{{kind.kind}}</button>
    </div>
    <hr>
  </section>
</template>

<script setup>
import axios from 'axios';
import {ref, defineEmits, onMounted} from 'vue';

const kinds = ref([])
const kindReceived=ref(null)
const emit = defineEmits(['getKind'])

const getKind = (kind) => {
    emit('getKind', kind);
}

onMounted(()=>{
  axios.get('http://127.0.0.1:8000/api/types/')
      .then(response => {
        kinds.value = response.data;
      })
      .catch(e => console.log(e));
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
