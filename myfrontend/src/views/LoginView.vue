<template>
  <div>
    <navbar-component/>
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="loginHandler">
      <br>
      <div style="margin-bottom: 13px;">
        <input v-model="username" placeholder="Username" required />
        <p v-if="usernameError" class="error">{{ usernameError }}</p>
      </div>
      <div>
        <input v-model="password" type="password" placeholder="Password" required />
        <p v-if="passwordError" class="error">{{ passwordError }}</p>
      </div>
      <br>
      <button type="submit">Inicio</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { login } from '@/auth';
import NavbarComponent from '@/components/NavbarComponent.vue';

const router = useRouter();
const username = ref('');
const password = ref('');
const usernameError = ref('');
const passwordError = ref('');

const loginHandler = async () => {
  // Reset errors
  usernameError.value = '';
  passwordError.value = '';

  try {
    const response = await axios.post('http://127.0.0.1:8000/api/token/', {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    login({username:username.value});
    router.push('/');
  } catch (error) {
    if (error.response && error.response.data) {
      // Assuming the backend returns an error response like:
      // { "detail": "Invalid credentials", "field": "username" }
      const errorMsg = error.response.data.detail || 'Invalid credentials';
      const errorField = error.response.data.field || 'general';

      if (errorField === 'username') {
        usernameError.value = errorMsg;
      } else if (errorField === 'password') {
        passwordError.value = errorMsg;
      } else {
        // General error handling if the field is not specified
        usernameError.value = errorMsg;
        passwordError.value = errorMsg;
      }
    } else {
      console.error(error);
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
  font-size: 0.875em;
}
</style>