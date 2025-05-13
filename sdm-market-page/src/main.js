import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Users from './components/Users.vue';
import Products from './components/Products.vue';
import Purchases from './components/Purchases.vue';

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
