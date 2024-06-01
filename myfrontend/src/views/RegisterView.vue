<template>
    <div>
    <br>
      <h1>Registro</h1>
      <br>
      <form @submit.prevent="register">
        <div style="margin-bottom: 13px;">
          <input v-model="username" placeholder="Username" required />
        </div>
        <div>
          <input v-model="password" type="password" placeholder="Password" required />
        </div>
        <br>
        <button type="submit">Registro</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  
  const router = useRouter();
  const username = ref('');
  const password = ref('');
  
  const register = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/api/register/', {
        username: username.value,
        password: password.value,
      });
      router.push('/login');
    } catch (error) {
      console.error(error);
    }
  };
  </script>
  