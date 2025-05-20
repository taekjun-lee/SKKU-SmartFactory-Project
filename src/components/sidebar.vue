<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>
  <div class="sidebar">
    <router-link to="/home" class="title-link">
      <h2 class="title">My App</h2>
    </router-link>

    <ul class="nav">
      <li><router-link to="/home">Home</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/settings">Settings</router-link></li>
      <li><router-link to="/help">Help</router-link></li>
    </ul>
  </div>
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100vh;
  background-color: #2c3e50;
  color: white;
  padding: 20px;
}

.title {
  font-size: 24px;
  margin-bottom: 40px;
  text-align: left;
}

.nav {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav li {
  margin-bottom: 25px;
}

.nav a {
  display: block;
  color: white;
  text-decoration: none;
  font-weight: 500;
  text-align: left;
  padding-left: 5px;
  transition: color 0.2s;
}

.nav a.router-link-exact-active {
  color: #42b983;
}
</style>