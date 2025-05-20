<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>
  <div class="sidebar">
    <router-link to="/dashboard" class="title-link">
      <h2 class="title">시스템 이름</h2>
    </router-link>

    <ul class="nav">
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/quality">품질 모니터링</router-link></li>
      <li><router-link to="/maintenance">고장 분석</router-link></li>
      <li><router-link to="/rawdata">데이터 샘플</router-link></li>
    </ul>
  </div>
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 200px;
  height: 100vh;
  background-color: #2c3e50;
  color: white;
  padding: 20px;
  box-sizing: border-box;
}

.title {
  font-size: 24px;
  margin-bottom: 40px;
  text-align: left;
  color: white;
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
  font-weight: bold;
}
</style>