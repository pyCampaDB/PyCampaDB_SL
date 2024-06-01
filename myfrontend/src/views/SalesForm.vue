<template>
    <navbar-component/>
    <div>
      <br>
      <h1>Comprar</h1>
      <br>
      <form @submit.prevent="register">
        <label for="example1" class="form-label" >Producto: </label>
        <select v-model="product" required class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
          <option style="text-align: center;" v-for="item in products" :key="item.product" :value="item.product">{{ item.product }}</option>
        </select>
        <div >
          <label for="example2" class="form-label">Cantidad:</label>
          <input style="text-align: center;" class="form-control" id="example1" v-model="amount" type="number" min="1" step="1" required />
        </div>
        <div>
          <label for="example3" class="form-label">Descuento:</label>
          <input style="text-align: center;" id="example3" class="form-control-plaintext" v-model="discount" type="number" value="20" placeholder="20" required readonly />
        </div>
        <br>
        <button type="submit">Comprar</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import NavbarComponent from '@/components/NavbarComponent.vue';
  import axios from 'axios';
  
  const router = useRouter();
  const products = ref([]); // Declarar products
  const product = ref('');
  const amount = ref('');
  const discount = ref('20');
  const client = ref(localStorage.getItem('username'));
  
  // Obtener la lista de productos al montar el componente
  onMounted(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/products/');
      products.value = response.data;
    } catch (error) {
      console.error(error);
    }
  });
  
  const register = async () => {
    try {
      const token = localStorage.getItem('access_token'); // Obtener el token desde localStorage
      await axios.post('http://127.0.0.1:8000/api/sale/new/', {
        product: product.value,
        client: client.value, // Usar el usuario autenticado
        amount: amount.value,
        discount: discount.value,
      }, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
      router.push('/sales');
    } catch (error) {
      console.error(error);
    }
  };
  </script>
  
  <style scoped>
  .form {
    margin-bottom: 13px;
    
  }
  </style>
  