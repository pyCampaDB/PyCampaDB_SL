<template>
  <navbar-component/>
  <assets-component/>
  
  
</template>
<script setup>
/*import axios from 'axios';
import NavbarComponent from '@/components/NavbarComponent.vue';
import AssetsComponent from '@/components/AssetsComponent.vue';
import {ref ,onMounted} from 'vue'
  
const assets = ref([])
const filteredassets=ref([]);
const videoReceived=ref(null);
const searchTextRule=ref(null)

const search = (searchText)=>{
videoReceived.value=null
searchTextRule.value=searchText
if(searchText) {
  filteredassets.value=assets.value.filter((asset)=>{
    const assetvideo = asset.video.toLowerCase();
    const searchTerm = searchText.toLowerCase();
    return assetvideo.includes(searchTerm)
  })
} else {
  filteredassets.value=assets.value
}
}

const video = (video)=>{
  searchTextRule.value=null
  videoReceived.value=video
  if(video) {
    filteredassets.value=assets.value.filter((asset)=>asset.video === video )
  } else {
    filteredassets.value=assets.value
  }
}

const resetFilter = () => {
videoReceived.value =null
searchTextRule.value=null
filteredassets.value=assets.value
}
onMounted (()=>{
  axios.get('http://127.0.0.1:8000/assets/').then(
    response => {
          assets.value=response.data
          filteredassets.value=assets.value
        }
      ).catch(e => {console.log(e)})
    })*/
    </script>

