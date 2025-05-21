<script setup>
import { ref, watch } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'
import Papa from 'papaparse'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const props = defineProps({
  selectedSensor: String
})

const chartData = ref(null)

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      title: { display: true, text: 'Timestamp' },
      ticks: {
        maxRotation: 45,
        minRotation: 45
      }
    },
    y: {
      title: { display: true, text: '' }
    }
  }
})

watch(() => props.selectedSensor, async (newSensor) => {
  if (!newSensor) {
    chartData.value = null
    return
  }

  const csvUrl = 'https://raw.githubusercontent.com/taekjun-lee/SKKU-SmartFactory-Data/refs/heads/main/TEST_DATA.csv'
  const response = await fetch(csvUrl)
  const csvText = await response.text()

  Papa.parse(csvText, {
    header: true,
    skipEmptyLines: true,
    complete: (results) => {
      const labels = []
      const values = []

      results.data.forEach(row => {
        if (row['Timestamp'] && row[newSensor]) {
          labels.push(row['Timestamp'])
          values.push(parseFloat(row[newSensor]))
        }
      })

      chartData.value = {
        labels,
        datasets: [
          {
            label: newSensor,
            data: values,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            tension: 0.3,
            fill: true
          }
        ]
      }

      chartOptions.value.scales.y.title.text = newSensor
    }
  })
}, { immediate: true })
</script>

<template>
  <div>
    <Line :data="chartData" :options="chartOptions" v-if="chartData" />
    <p v-else>센서를 선택해주세요...</p>
  </div>
</template>

<style scoped>
div {
  height: 400px;
  padding: 20px;
}
</style>
