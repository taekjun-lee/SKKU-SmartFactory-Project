<script setup>
import { ref, onMounted, defineEmits } from 'vue'

const emit = defineEmits(['sensor-selected'])

const headers = ref([])
const selectedHeader = ref('') // 선택된 항목 저장

onMounted(async () => {
  const csvUrl = 'https://raw.githubusercontent.com/taekjun-lee/SKKU-SmartFactory-Data/refs/heads/main/TEST_DATA.csv'
  const response = await fetch(csvUrl)
  const text = await response.text()

  const lines = text.split('\n')
  if (lines.length > 0) {
    const rawHeader = lines[0].trim()
    const allHeaders = rawHeader.split(',')
    headers.value = allHeaders.slice(2, 7) // Sensor_A~Sensor_E
  }
})

function selectSensor(header) {
  selectedHeader.value = header
  emit('sensor-selected', header)
}
</script>

<template>
  <!-- 날짜 필터
  <div class="filter">
    <label>시작:</label>
    <input type="datetime-local" v-model="startTime" />
    <label>종료:</label>
    <input type="datetime-local" v-model="endTime" />
    <button @click="applyFilter">필터 적용</button>
  </div>
  -->

  <div class="header">Parameter 목록</div>
  <div class="parameterlist">
    <ul v-if="headers.length">
      <li
        v-for="(header, index) in headers"
        :key="index"
        @click="selectSensor(header)"
        :class="{ selected: selectedHeader === header }"
        style="cursor: pointer;"
      >
        {{ header }}
      </li>
    </ul>
    <p v-else>헤더를 불러오는 중입니다...</p>
  </div>
</template>

<style scoped>
.header {
  font-weight: bold;
  border-bottom: 1px solid #eee;
}

.parameterlist {
  overflow-y: auto;
  border-radius: 8px;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  padding: 6px 8px;
  border-bottom: 1px solid #eee;
  font-family: monospace;
  transition: background-color 0.2s;
}

li.selected {
  background-color: #cce5ff;
  font-weight: bold;
  color: #003366;
}
</style>