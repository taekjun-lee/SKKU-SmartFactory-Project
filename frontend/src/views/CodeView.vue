<template>
  <div class="code">
    <h2>Code 구성 및 요약</h2>
  </div>
  <div class="code-grid">
    <div class="api">
      <div class="header">API
        <div class="fileview">📁</div>
      </div>
      <div class="contents-container">
        <div class="contents-header">
          Python 기반 FastAPI
        </div>
        <div class="contents">
          <p>dfdfdf</p>
          <p>dfdfdf</p>
          <p>dfdfdf</p>
        </div>
      </div>
    </div>
    <div class="analysis">
      <div class="header">Data 분석
        <div class="fileview">📁</div>
      </div>
      <div class="contents-container">
        <div class="contents-header">
          Python 기반 FastAPI
        </div>
        <div class="contents">
          <p>dfdfdf</p>
          <p>dfdfdf</p>
          <p>dfdfdf</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.code {
  padding: 6px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.code-grid {
  display: grid;
  grid-template-columns: 825px 825px;
  gap: 6px;
}

.code-grid > div {
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.analysis {
  background-color: white;
  padding: 6px;
  border-radius: 8px;
  text-align: left;
  line-height: 28px;
}

.api {
  background-color: white;
  padding: 6px;
  border-radius: 8px;
  text-align: left;
  line-height: 28px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  border-bottom: 2px solid #aaa;
  text-align: center;
  font-size: 18px;
}

.fileview {
  margin-left: 10px;
  cursor: pointer;
}

.contents-container {
  margin: 8px;
  padding-left: 6px;
}

.contents-header {
  font-size: 16px;
  font-weight: bold;
}

.contents {
  font-size: 14px;
}
</style>