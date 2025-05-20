<template>
  <div class="dashboard">
    <h1>샘플 데이터 Google docs API test</h1>
    <p>데이터 수량이 많아지면 많아질수록 느리고 렉걸릴듯</p>

    <div class="table-container">
      <table class="styled-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>설비명</th>
            <th>상태</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in paginatedData"
            :key="item.ID"
            :class="getStatusClass(item.Status)"
          >
            <td>{{ item.ID }}</td>
            <td>{{ item.Name }}</td>
            <td>{{ item.Status }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="pagination">
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
  return lines.slice(1).map(line => {
    const values = line.split(',')
    const obj = {}
    headers.forEach((header, i) => {
      obj[header.trim()] = values[i]?.trim() ?? ''
    })
    return obj
  })
}

onMounted(async () => {
  const response = await fetch("https://docs.google.com/spreadsheets/d/e/2PACX-1vR_IUp2JX2R5MKqF_In41vy0Tk-oaxwIvtMuYNTAgrOsuo7bf20wUrdL7qH-61abR6qx920hnOIVYkV/pub?output=csv")
  const text = await response.text()
  sensorData.value = parseCSV(text)
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
</style>