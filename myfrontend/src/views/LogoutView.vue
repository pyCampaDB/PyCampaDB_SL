<template>
    <button @click="logout">Logout</button>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  import { logout } from '@/auth';
  
  const router = useRouter();
  
  const logoutHandler = () => {
    logout();
    router.push('/login');
  };
  </script>
  