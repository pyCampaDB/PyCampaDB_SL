<template>
  <navbar-component @getSearchText="search"/>
  <navigation-component @getKind="kind" />

  <div class="mb-3" v-if="searchTextRule">
    <h3>Productos con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los productos</button>
  <div class="alert alert-warning" role="alert" v-if="filteredProducts.length===0">De <strong>{{searchTextRule}}</strong> me quedao a cero pisha</div>
  </div>
  <div class="mb-3" v-if="kindReceived">
    <h3>Productos de <strong>{{ kindReceived }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los productos</button>
  <div class="alert alert-warning" role="alert" v-if="filteredProducts.length===0">De <strong>{{kindReceived}}</strong> me quedao a cero pisha</div>
  </div>
  <div>
    <div class="row row-cols-1 row-cols-md-3 g-4 justify-content-center">
        <div class="col" v-for="product in filteredProducts" :key="product.id">
          <div class="card text-center mx-auto">
            <div class="card-body">
              <img :src="product.image" class="card-img-top" alt="Imagen de {{ product.product }}" >
              <h5 class="card-title">{{product.product}}</h5>
              <h6 class="card-subtitle mb-2 text-body-secondary">{{product.kind}}</h6>
              <p class="card-text">{{product.description}}</p>
            </div>
            <div class="card-footer text-danger">{{product.price}} {{ product.currency_type }}</div>
        </div>
      </div>
    </div>
  </div>
  <br><br>
  <button class="btn btn-lg btn-warning"><router-link class="nav-link active" aria-current="page" to="/sale/new">Comprar Producto</router-link></button>
  
</template>

<script setup>
import axios from 'axios';
import NavigationComponent from '@/components/NavigationComponent.vue';
import NavbarComponent from '@/components/NavbarComponent.vue';
import {ref, onMounted} from 'vue'
  
const products= ref([]);
const filteredProducts=ref([]);
const kindReceived= ref(null);
const searchTextRule=ref(null)

const search = (searchText)=>{
  kindReceived.value=null
  searchTextRule.value=searchText
  if(searchText) {
    filteredProducts.value=products.value.filter((product)=>{
      const productName = product.product.toLowerCase();
      const productDescription = product.description.toLowerCase();
      const searchTerm = searchText.toLowerCase();
      return (productName.includes(searchTerm) || productDescription.includes(searchTerm))
        
      
    })
  } else {
    filteredProducts.value=products.value
  }
}     
const kind = (kind)=>{
  searchTextRule.value=null
  kindReceived.value=kind
  if(kind) {
    filteredProducts.value=products.value.filter((product)=>product.kind === kind )
  } else {
    filteredProducts.value=products.value
  }
}
const resetFilter = () => {
  kindReceived.value =null
  searchTextRule.value=null
  filteredProducts.value=products.value
}
onMounted (()=>{
  axios.get('http://localhost:8000/api/products/').then(
    response => {
          products.value=response.data
          filteredProducts.value=products.value
        }
      ).catch(e => {console.log(e)})
    })
  
  
</script>
<style>
.card {
  border: 2px solid gray;
}
</style>