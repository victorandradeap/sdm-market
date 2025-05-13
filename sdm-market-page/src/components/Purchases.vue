<template>
  <div>
    <h2>Purchases</h2>
    
    <!-- Form to add new purchase -->
    <div class="card mb-4">
      <div class="card-header">
        New Purchase
      </div>
      <div class="card-body">
        <form @submit.prevent="savePurchase">
          <div class="form-group">
            <label for="userId">Customer</label>
            <select class="form-control" id="userId" v-model="purchase.user_id" required>
              <option value="">Select a customer</option>
              <option v-for="user in users" :key="user.id" :value="user.id">{{ user.name }}</option>
            </select>
          </div>
          
          <div class="mt-4 mb-3">
            <h5>Products</h5>
            <div v-for="(item, index) in purchase.products" :key="index" class="card mb-3">
              <div class="card-body">
                <div class="row">
                  <div class="col-md-5">
                    <div class="form-group">
                      <label :for="'product' + index">Product</label>
                      <select class="form-control" :id="'product' + index" v-model="item.product_id" required>
                        <option value="">Select a product</option>
                        <option v-for="product in products" :key="product.id" :value="product.id">
                          {{ product.name }} ({{ formatCurrency(product.price) }})
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="col-md-3">
                    <div class="form-group">
                      <label :for="'quantity' + index">Quantity</label>
                      <input type="number" class="form-control" :id="'quantity' + index" v-model="item.quantity" min="1" required>
                    </div>
                  </div>
                  <div class="col-md-2">
                    <div class="form-group">
                      <label>Unit Price</label>
                      <p class="form-control-static">{{ formatCurrency(item.unit_price) }}</p>
                    </div>
                  </div>
                  <div class="col-md-2">
                    <label class="d-block">&nbsp;</label>
                    <button type="button" class="btn btn-danger" @click="removeProduct(index)">Remove</button>
                  </div>
                </div>
              </div>
            </div>
            <button type="button" class="btn btn-secondary" @click="addProduct">Add Product</button>
          </div>
          
          <button type="submit" class="btn btn-primary mt-3">Complete Purchase</button>
        </form>
      </div>
    </div>
    
    <!-- Purchase list -->
    <div class="card">
      <div class="card-header">
        Purchase List
      </div>
      <div class="card-body">
        <div v-if="loading">Loading...</div>
        <div v-else-if="purchases.length === 0">No purchases registered.</div>
        <div v-else>
          <div v-for="purchase in purchases" :key="purchase.id" class="card mb-3">
            <div class="card-header d-flex justify-content-between align-items-center">
              <div>
                Purchase #{{ purchase.id }} - {{ formatDate(purchase.purchase_date) }} - 
                Customer: {{ getUserName(purchase.user_id) }}
              </div>
              <button class="btn btn-sm btn-danger" @click="deletePurchase(purchase.id)">Delete</button>
            </div>
            <div class="card-body">
              <table class="table table-sm">
                <thead>
                  <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Unit Price</th>
                    <th>Subtotal</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in purchase.products" :key="item.product_id">
                    <td>{{ getProductName(item.product_id) }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ formatCurrency(item.unit_price || 0) }}</td>
                    <td>{{ formatCurrency((item.unit_price || 0) * item.quantity) }}</td>
                  </tr>
                </tbody>
                <tfoot>
                  <tr>
                    <th colspan="3" class="text-end">Total:</th>
                    <th>{{ formatCurrency(purchase.total_amount) }}</th>
                  </tr>
                </tfoot>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Purchases',
  data() {
    return {
      purchases: [],
      users: [],
      products: [],
      purchase: {
        user_id: '',
        products: [{ product_id: '', quantity: 1, unit_price: 0 }]
      },
      loading: false
    }
  },
  mounted() {
    this.loadUsers();
    this.loadProducts();
    this.loadPurchases();
  },
  methods: {
    loadPurchases() {
      this.loading = true;
      axios.get('/api/purchases')
        .then(response => {
          // Process purchase data to ensure it has all required fields
          this.purchases = response.data.map(purchase => {
            // Make sure products have unit_price (use price as fallback)
            if (purchase.products) {
              purchase.products = purchase.products.map(product => {
                return {
                  ...product,
                  unit_price: product.unit_price || product.price || 0
                };
              });
            }
            return purchase;
          });
          this.loading = false;
        })
        .catch(error => {
          console.error('Error loading purchases:', error);
          this.loading = false;
        });
    },
    loadUsers() {
      axios.get('/api/users')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error('Error loading customers:', error);
        });
    },
    loadProducts() {
      axios.get('/api/products')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error loading products:', error);
        });
    },
    addProduct() {
      this.purchase.products.push({ product_id: '', quantity: 1, unit_price: 0 });
    },
    removeProduct(index) {
      if (this.purchase.products.length > 1) {
        this.purchase.products.splice(index, 1);
      }
    },
    savePurchase() {
      // Validate form
      if (!this.purchase.user_id || !this.purchase.products.some(p => p.product_id && p.quantity > 0)) {
        alert('Please fill in all fields.');
        return;
      }
      
      // Filter valid products and add unit price
      const products = this.purchase.products
        .filter(p => p.product_id && p.quantity > 0)
        .map(p => {
          // Find the selected product to get its price
          const product = this.products.find(prod => prod.id === p.product_id);
          return {
            product_id: p.product_id,
            quantity: p.quantity,
            unit_price: product ? product.price : 0 // Add unit_price from the product data
          };
        });
      
      // Create purchase object
      const purchaseData = {
        user_id: this.purchase.user_id,
        products: products
      };
      
      axios.post('/api/purchases', purchaseData)
        .then(() => {
          this.resetForm();
          this.loadPurchases();
          alert('Purchase registered successfully!');
        })
        .catch(error => {
          console.error('Error registering purchase:', error);
          alert('Error registering purchase. Check the console for more details.');
        });
    },
    resetForm() {
      this.purchase = {
        user_id: '',
        products: [{ product_id: '', quantity: 1, unit_price: 0 }]
      };
    },
    deletePurchase(id) {
      if (confirm('Are you sure you want to delete this purchase?')) {
        axios.delete(`/api/purchases/${id}`)
          .then(() => {
            this.loadPurchases();
          })
          .catch(error => {
            console.error('Error deleting purchase:', error);
          });
      }
    },
    getUserName(userId) {
      if (!userId) return 'Unknown Customer';
      const user = this.users.find(u => u.id === userId);
      return user ? user.name : `Customer #${userId}`;
    },
    getProductName(productId) {
      if (!productId) return 'Unknown Product';
      const product = this.products.find(p => p.id === productId);
      return product ? product.name : `Product #${productId}`;
    },
    formatCurrency(value) {
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(value);
    },
    formatDate(dateString) {
      if (!dateString) return 'No date';
      try {
        return new Date(dateString).toLocaleDateString();
      } catch (e) {
        return 'Invalid Date';
      }
    },
    // Helper method to update unit_price when a product is selected
    updateProductPrice(index) {
      const selectedProductId = this.purchase.products[index].product_id;
      if (selectedProductId) {
        const product = this.products.find(p => p.id === selectedProductId);
        if (product) {
          this.purchase.products[index].unit_price = product.price;
        }
      } else {
        this.purchase.products[index].unit_price = 0;
      }
    }
  },
  watch: {
    // Watch for changes to product selections and update prices
    'purchase.products': {
      handler(products) {
        products.forEach((product, index) => {
          if (product.product_id) {
            this.updateProductPrice(index);
          }
        });
      },
      deep: true
    }
  }
}
</script>
