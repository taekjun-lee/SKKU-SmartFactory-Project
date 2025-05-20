<template>
  <div class="full-page">
    <div class="row-title">품질 트렌드 요약</div>
    <div class="row">
      <div class="grid-item">설비 품질 차트 영역</div>
      <div class="grid-item">Parameter 목록, 스펙 등 정보</div>
    </div>

    <div class="row-title">고장 이력 및 분석</div>
    <div class="row">
      <div class="grid-item">설비 이상 여부 및 이전 고장 이력</div>
      <div class="grid-item">이상 있을 시 원인 분석 결과 화면</div>
    </div>

    <div class="row-title">생각해봐야할듯</div>
    <div class="row">
      <div class="grid-item">생각해봐야할듯</div>
      <div class="grid-item">생각해봐야할듯</div>
    </div>
  </div>
</template>

<script setup>
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
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 500px;
  min-height: 200px;
}
</style>