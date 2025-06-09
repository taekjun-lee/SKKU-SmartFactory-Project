<script setup>
import { ref, watch, nextTick } from 'vue'
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
import zoomPlugin from 'chartjs-plugin-zoom'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  zoomPlugin
)

const props = defineProps({
  selectedSensor: String
})

const chartData = ref(null)
const chartOptions = ref({})
let chartInstance = null

function zoomIn() {
  if (chartInstance) chartInstance.zoom(1.05)
}
function zoomOut() {
  if (chartInstance) chartInstance.zoom(0.95)
}
function panLeft() {
  if (chartInstance) chartInstance.pan({ x: 10 })
}
function panRight() {
  if (chartInstance) chartInstance.pan({ x: -10 })
}

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
            data: values,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            tension: 0.1,
            fill: true,
            pointRadius: 1,
            pointHoverRadius: 6,
            borderWidth: 1
          }
        ]
      }

      chartOptions.value = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          zoom: {
            zoom: {
              wheel: { enabled: true },
              pinch: { enabled: true },
              mode: 'x',
              onZoom: ({ chart }) => {
                chart.options.scales.y.min = undefined
                chart.update('none')
              },
              onZoomComplete: ({ chart }) => {
                const currentMin = chart.scales.x.min
                const currentMax = chart.scales.x.max
                const fullMin = 0
                const fullMax = 999
                if (currentMin <= fullMin && currentMax >= fullMax) {
                  chart.options.scales.y.min = 0
                  chart.update('none')
                }
              }
            },
            pan: {
              enabled: true,
              mode: 'x'
            },
            limits: {
              x: { min: 0, max: labels.length - 1 }
            }
          }
        },
        scales: {
          x: {
            title: { display: false },
            ticks: {
              minRotation: 45,
              autoSkip: true,
              maxTicksLimit: 20,
              callback: function (value) {
                const label = this.getLabelForValue(value)
                const [datePart, timePart] = label.split(' ')
                const [year, month, day] = datePart.split('-')
                const [hour, minute] = timePart.split(':')
                const paddedHour = hour.padStart(2, '0')
                const paddedMinute = minute.padStart(2, '0')
                return `${year.slice(2)}-${month}-${day} ${paddedHour}:${paddedMinute}`
              }
            },
            min: 0,
            max: 999
          },
          y: {
            title: { display: false },
            min: 0
          }
        }
      }

      nextTick(() => {
        const chart = ChartJS.getChart(document.querySelector('canvas'))
        if (chart) chartInstance = chart
      })
    }
  })
}, { immediate: true })
</script>

<template>
  <div class="chart-container">
    <div class="chart-toolbar">
      <button @click="zoomIn">🔍+</button>
      <button @click="zoomOut">🔍-</button>
      <button @click="panLeft">⬅️</button>
      <button @click="panRight">➡️</button>
    </div>
    <Line :data="chartData" :options="chartOptions" v-if="chartData" />
    <div v-else class="placeholder">
      <p>📌 Parameter를 선택해주세요</p>
    </div>
  </div>
</template>


<style scoped>
.chart-container {
  height: 400px;
  position: relative;
}

.placeholder {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 600;
  border-radius: 8px;
  text-align: center;
}

.chart-toolbar {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

.chart-toolbar button {
  background-color: #2c3e50;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.chart-toolbar button:hover {
  background-color: #1abc9c;
}
</style>
