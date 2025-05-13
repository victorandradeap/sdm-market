<template>
  <div class="container py-4">
    <header class="pb-3 mb-4 border-bottom">
      <h1 class="fs-4">Sistema de Gerenciamento de Vendas</h1>
    </header>

    <div class="row">
      <div class="col-md-3">
        <ul class="nav nav-pills flex-column mb-auto">
          <li class="nav-item">
            <router-link to="/users" class="nav-link" active-class="active">Clientes</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/products" class="nav-link" active-class="active">Produtos</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/purchases" class="nav-link" active-class="active">Compras</router-link>
          </li>
        </ul>
      </div>

      <div class="col-md-9">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
