<template>
  <navbar-component @getSearchsales="search"/>
  <assets-component />
  <div v-for="(sales, username) in groupedSales" :key="username">
    <h3 style="margin-top: 15px;">Compras de <strong>{{ username }}</strong></h3></div>
    <div class="mb-3" v-if="searchTextRule">
    <h3>Ventas con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todas los ventas</button>
    <div class="alert alert-warning" role="alert" v-if="filteredsales.length === 0">De <strong>{{searchTextRule}}</strong> me quedao a cero pisha</div>
  </div>
  <div class="mb-3" v-if="productReceived">
    <h3>Productos de <strong>{{ productReceived }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los productos</button>
    <div class="alert alert-warning" role="alert" v-if="filteredsales.length === 0">De <strong>{{productReceived}}</strong> me quedao a cero pisha</div>
  </div>
  <div>
    <div class="row row-cols-1 row-cols-md-3 g-4 justify-content-center">
      <div class="col" v-for="sale in filteredsales" :key="sale.id">
        <div class="card text-center mx-auto">
          <div class="card-body">
            <h5 class="card-product"> {{ sale.product.product }}</h5>
            <img :src="sale.product.image" class="card-img-top" alt="Imagen de {{ sale.product.product }}">
            <br>
            <p style="margin-top: 30px;margin-bottom: 13px;">{{ sale.product.description }}</p>
            <p>Cantidad: {{sale.amount}}. Importe: <strong style="color: brown;">{{ sale.price_final }}{{ sale.product.currency_type }}</strong></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import NavbarComponent from '@/components/NavbarComponent.vue';
import AssetsComponent from '@/components/AssetsComponent.vue';
import { ref, onMounted,computed } from 'vue';

const sales = ref([]);
const filteredsales = ref([]);
const productReceived = ref(null);
const searchTextRule = ref(null);

const search = (searchText) => {
  productReceived.value = null;
  searchTextRule.value = searchText;
  if (searchText) {
    filteredsales.value = sales.value.filter((sale) => {
      return sale.product === searchText;
    });
  } else {
    filteredsales.value = sales.value;
  }
};

const resetFilter = () => {
  productReceived.value = null;
  searchTextRule.value = null;
  filteredsales.value = sales.value;
};

const groupedSales = computed(() => {
  return filteredsales.value.reduce((acc, sale) => {
    const username = sale.client.username;
    if (!acc[username]) {
      acc[username] = [];
    }
    acc[username].push(sale);
    return acc;
  }, {});
});

onMounted(() => {
  const token = localStorage.getItem('access_token'); 
  if (token) {
    axios.get('http://localhost:8000/api/sales/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then(response => {
      sales.value = response.data;
      filteredsales.value = sales.value;
    }).catch(e => {
      if (e.response && e.response.status === 401) {
        console.error('Unauthorized. Please check the token.');
        window.location.href = '/login';
      } else {
        console.error('An error occurred:', e.response ? e.response.data : e.message);
      }
    });
  } else {
    console.log("User is not authenticated");
    window.location.href = '/login';
  }
});
</script>
