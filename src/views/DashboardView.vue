<template>
  <div class="full-page">
    <div class="row-title">품질 트렌드 요약</div>
    <div class="row">
      <ParameterInfo @sensor-selected="selectedSensor = $event" class="grid-item" />
      <QualityChart :selectedSensor="selectedSensor" class="grid-item" />
    </div>

    <div class="row-title">고장 이력 및 분석</div>
    <div class="row">
      <FailureHistory class="grid-item" />
      <FailureAnalysis class="grid-item" />
    </div>

    <div class="row-title">생각해봐야할듯</div>
    <div class="row">
      <Reserved1 class="grid-item" />
      <Reserved2 class="grid-item" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import QualityChart from '../components/QualityChart.vue'
import ParameterInfo from '../components/ParameterInfo.vue'
import FailureHistory from '../components/FailureHistory.vue'
import FailureAnalysis from '../components/FailureAnalysis.vue'
import Reserved1 from '../components/Reserved1.vue'
import Reserved2 from '../components/Reserved2.vue'

const selectedSensor = ref('')
</script>

<style scoped>
.full-page {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.row-title {
  font-weight: bold;
  font-size: 18px;
  background-color: #2c3e50;
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
}

.row-title > *:not(:first-child) {
  margin-top: 16px;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 12px;
  margin-bottom: 12px;
}

.grid-item {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  font-weight: bold;
  font-size: 16px;
  text-align: center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  min-width: 500px;
  min-height: 200px;
}
</style>