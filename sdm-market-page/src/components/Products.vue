<template>
  <div>
    <h2>Products</h2>
    
    <!-- Form to add/edit product -->
    <div class="card mb-4">
      <div class="card-header">
        {{ editingProduct ? 'Edit Product' : 'Add New Product' }}
      </div>
      <div class="card-body">
        <form @submit.prevent="saveProduct">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" v-model="currentProduct.name" required>
          </div>
          <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" v-model="currentProduct.description"></textarea>
          </div>
          <div class="form-group">
            <label for="price">Price</label>
            <input type="number" class="form-control" id="price" v-model="currentProduct.price" min="0.01" step="0.01" required>
          </div>
          <button type="submit" class="btn btn-primary">{{ editingProduct ? 'Update' : 'Add' }}</button>
          <button v-if="editingProduct" type="button" class="btn btn-secondary ms-2" @click="cancelEdit">Cancel</button>
        </form>
      </div>
    </div>
    
    <!-- Product list -->
    <div class="card">
      <div class="card-header">
        Product List
      </div>
      <div class="card-body">
        <div v-if="loading">Loading...</div>
        <div v-else-if="products.length === 0">No products registered.</div>
        <table v-else class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Price</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in products" :key="product.id">
              <td>{{ product.id }}</td>
              <td>{{ product.name }}</td>
              <td>{{ product.description }}</td>
              <td>{{ formatCurrency(product.price) }}</td>
              <td>
                <button class="btn btn-sm btn-primary btn-action" @click="editProduct(product)">Edit</button>
                <button class="btn btn-sm btn-danger btn-action" @click="deleteProduct(product.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Products',
  data() {
    return {
      products: [],
      currentProduct: {
        name: '',
        description: '',
        price: 0
      },
      editingProduct: null,
      loading: false
    }
  },
  mounted() {
    this.loadProducts();
  },
  methods: {
    loadProducts() {
      this.loading = true;
      axios.get(`${process.env.SDM_MARKET_API_URL || 'http://localhost:5000'}/api/products`)
        .then(response => {
          this.products = response.data;
          this.loading = false;
        })
        .catch(error => {
          console.error('Error loading products:', error);
          this.loading = false;
        });
    },
    saveProduct() {
      if (this.editingProduct) {
        // Update existing product
        axios.put(`${process.env.SDM_MARKET_API_URL || 'http://localhost:5000'}/api/products/${this.editingProduct.id}`, this.currentProduct)
          .then(() => {
            this.loadProducts();
            this.resetForm();
          })
          .catch(error => {
            console.error('Error updating product:', error);
          });
      } else {
        // Add new product
        axios.post(`${process.env.SDM_MARKET_API_URL || 'http://localhost:5000'}/api/products`, this.currentProduct)
          .then(() => {
            this.loadProducts();
            this.resetForm();
          })
          .catch(error => {
            console.error('Error adding product:', error);
          });
      }
    },
    editProduct(product) {
      this.editingProduct = product;
      this.currentProduct = { ...product };
    },
    cancelEdit() {
      this.resetForm();
    },
    resetForm() {
      this.currentProduct = {
        name: '',
        description: '',
        price: 0
      };
      this.editingProduct = null;
    },
    deleteProduct(id) {
      if (confirm('Are you sure you want to delete this product?')) {
        axios.delete(`${process.env.SDM_MARKET_API_URL || 'http://localhost:5000'}/api/products/${id}`)
          .then(() => {
            this.loadProducts();
          })
          .catch(error => {
            console.error('Error deleting product:', error);
          });
      }
    },
    formatCurrency(value) {
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(value);
    }
  }
}
</script>
