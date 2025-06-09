<template>
  <div class="dashboard">
    <h1>센서 데이터 불러오기 테스트</h1>
    <p>CSV 용량이 커서 로딩 시간이 걸릴 수 있습니다</p>

    <div v-if="isLoading" class="loading">
      <div class="spinner-circle"></div>
      <p>데이터 로딩 중입니다...</p>
    </div>

    <div v-else class="table-container">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Sensor_A</th>
            <th>Sensor_B</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in paginatedData"
            :key="item.Timestamp"
          >
            <td>{{ item.Timestamp }}</td>
            <td>{{ item.SensorA }}</td>
            <td>{{ item.SensorB }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="pagination" v-if="!isLoading">
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const sensorData = ref([])
const currentPage = ref(1)
const itemsPerPage = 20

function parseCSV(text) {
  const lines = text.trim().split('\n')
  const headers = lines[0].split(',')
  const timestampIndex = headers.indexOf('Timestamp')
  const sensoraIndex = headers.indexOf('Sensor_A')
  const sensorbIndex = headers.indexOf('Sensor_B')

  return lines.slice(1).map(line => {
    const values = line.split(',')
    return {
      Timestamp: values[timestampIndex],
      SensorA: values[sensoraIndex],
      SensorB: values[sensorbIndex]
    }
  })
}

const isLoading = ref(true)
onMounted(async () => {
  isLoading.value = true
  try {
    const response = await fetch("https://raw.githubusercontent.com/taekjun-lee/SKKU-SmartFactory-Data/refs/heads/main/TEST_DATA.csv")
    const text = await response.text()
    sensorData.value = parseCSV(text)
  } catch (error) {
    console.error("CSV 불러오기 실패:", error)
  } finally {
    isLoading.value = false
  }
})

const totalPages = computed(() => Math.ceil(sensorData.value.length / itemsPerPage))

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return sensorData.value.slice(start, start + itemsPerPage)
})

function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++
}

function prevPage() {
  if (currentPage.value > 1) currentPage.value--
}

function getStatusClass(status) {
  switch (status?.toLowerCase()) {
    case 'normal':
      return 'status-normal'
    case 'alert':
      return 'status-alert'
    case 'error':
      return 'status-error'
    default:
      return ''
  }
}
</script>

<style scoped>
.dashboard {
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 16px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.styled-table thead {
  background-color: #333;
  color: white;
}

.styled-table th,
.styled-table td {
  padding: 12px 16px;
  border: 1px solid #ddd;
}

.styled-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.status-normal {
  background-color: #e0f7e9;
  color: #2e7d32;
  font-weight: bold;
}

.status-alert {
  background-color: #fff3cd;
  color: #d35400;
  font-weight: bold;
}

.status-error {
  background-color: #fdecea;
  color: #c0392b;
  font-weight: bold;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 10px;
}

.pagination button {
  padding: 8px 12px;
  background-color: #333;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 6px;
}

.pagination button:disabled {
  background-color: #999;
  cursor: not-allowed;
}

.pagination span {
  font-weight: bold;
}

.loading {
  margin-top: 40px;
  font-size: 18px;
  color: #555;
  text-align: center;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.spinner-circle {
  width: 40px;
  height: 40px;
  border: 6px solid #ddd;
  border-top-color: #333;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 10px;
}
</style>