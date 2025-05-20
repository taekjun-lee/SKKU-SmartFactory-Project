import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import QualityView from '../views/QualityView.vue'
import MaintenanceView from '../views/MaintenanceView.vue'
import RawdataView from '../views/RawdataView.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', component: DashboardView },
  { path: '/quality', component: QualityView },
  { path: '/maintenance', component: MaintenanceView },
  { path: '/rawdata', component: RawdataView }
]

const router = createRouter({
  history: createWebHistory('/SKKU-SmartFactory-Project/'),
  routes
})

export default router