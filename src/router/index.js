import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import SettingsView from '../views/SettingsView.vue'
import HelpView from '../views/HelpView.vue'

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: HomeView },
  { path: '/dashboard', component: DashboardView },
  { path: '/settings', component: SettingsView },
  { path: '/help', component: HelpView }
]

const router = createRouter({
  history: createWebHistory('/SKKU-SmartFactory-Project/'),
  routes
})

export default router