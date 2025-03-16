
<template>
  <!--  <nav>-->
  <!--    <router-link to="/">Home</router-link> |-->
  <!--    <router-link to="/authorization">Authorization</router-link> |-->
  <!--    <router-link to="/register">Registration</router-link>-->
  <!--  </nav>-->
    <router-view/>
  </template>
  
  <style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  
  
  nav {
    padding: 30px;
  }
  
  nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  
  
  body {
    margin: 0;
  }
  </style>
  <script setup lang="ts">
  </script>