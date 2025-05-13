import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import axios from 'axios';
import App from './App.vue';
import Users from './components/Users.vue';
import Products from './components/Products.vue';
import Purchases from './components/Purchases.vue';

// Configure axios for API requests
const apiUrl = process.env.SDM_MARKET_API_URL || '';
if (apiUrl) {
  axios.defaults.baseURL = apiUrl;
}

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/users' },
    { path: '/users', component: Users },
    { path: '/products', component: Products },
    { path: '/purchases', component: Purchases },
  ]
});

const app = createApp(App);
app.use(router);
app.mount('#app');
