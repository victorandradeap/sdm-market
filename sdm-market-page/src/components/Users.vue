<template>
  <div>
    <h2>Customers</h2>
    
    <!-- Form to add/edit customer -->
    <div class="card mb-4">
      <div class="card-header">
        {{ editingUser ? 'Edit Customer' : 'Add New Customer' }}
      </div>
      <div class="card-body">
        <form @submit.prevent="saveUser">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" v-model="currentUser.name" required>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="currentUser.email" required>
          </div>
          <div class="form-group">
            <label for="phone">Phone</label>
            <input type="text" class="form-control" id="phone" v-model="currentUser.phone" required>
          </div>
          <button type="submit" class="btn btn-primary">{{ editingUser ? 'Update' : 'Add' }}</button>
          <button v-if="editingUser" type="button" class="btn btn-secondary ms-2" @click="cancelEdit">Cancel</button>
        </form>
      </div>
    </div>
    
    <!-- Customer list -->
    <div class="card">
      <div class="card-header">
        Customer List
      </div>
      <div class="card-body">
        <div v-if="loading">Loading...</div>
        <div v-else-if="users.length === 0">No customers registered.</div>
        <table v-else class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.id }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.phone }}</td>
              <td>
                <button class="btn btn-sm btn-primary btn-action" @click="editUser(user)">Edit</button>
                <button class="btn btn-sm btn-danger btn-action" @click="deleteUser(user.id)">Delete</button>
                <button class="btn btn-sm btn-info" @click="viewUserPurchases(user.id)">View Purchases</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- User purchases modal -->
    <div v-if="showUserPurchases" class="modal d-block" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Customer Purchases</h5>
            <button type="button" class="btn-close" @click="showUserPurchases = false"></button>
          </div>
          <div class="modal-body">
            <div v-if="loadingPurchases">Loading purchases...</div>
            <div v-else-if="userPurchases.length === 0">This customer has no purchases.</div>
            <div v-else>
              <div v-for="purchase in userPurchases" :key="purchase.id" class="card mb-3">
                <div class="card-header">
                  Purchase #{{ purchase.id }} - {{ formatDate(purchase.purchase_date) }}
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
                        <td>{{ item.product_name || 'Product #' + item.product_id }}</td>
                        <td>{{ item.quantity }}</td>
                        <td>{{ formatCurrency(item.unit_price || item.price || 0) }}</td>
                        <td>{{ formatCurrency((item.unit_price || item.price || 0) * item.quantity) }}</td>
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
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="showUserPurchases = false">Close</button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showUserPurchases" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Users',
  data() {
    return {
      users: [],
      currentUser: {
        name: '',
        email: '',
        phone: ''
      },
      editingUser: null,
      loading: false,
      showUserPurchases: false,
      userPurchases: [],
      loadingPurchases: false
    }
  },
  mounted() {
    this.loadUsers();
  },
  methods: {
    loadUsers() {
      this.loading = true;
      axios.get('/api/users')
        .then(response => {
          this.users = response.data;
          this.loading = false;
        })
        .catch(error => {
          console.error('Error loading customers:', error);
          this.loading = false;
        });
    },
    saveUser() {
      if (this.editingUser) {
        // Update existing customer
        axios.put(`/api/users/${this.editingUser.id}`, this.currentUser)
          .then(() => {
            this.loadUsers();
            this.resetForm();
          })
          .catch(error => {
            console.error('Error updating customer:', error);
          });
      } else {
        // Add new customer
        axios.post('/api/users', this.currentUser)
          .then(() => {
            this.loadUsers();
            this.resetForm();
          })
          .catch(error => {
            console.error('Error adding customer:', error);
          });
      }
    },
    editUser(user) {
      this.editingUser = user;
      this.currentUser = { ...user };
    },
    cancelEdit() {
      this.resetForm();
    },
    resetForm() {
      this.currentUser = {
        name: '',
        email: '',
        phone: ''
      };
      this.editingUser = null;
    },
    deleteUser(id) {
      if (confirm('Are you sure you want to delete this customer?')) {
        axios.delete(`/api/users/${id}`)
          .then(() => {
            this.loadUsers();
          })
          .catch(error => {
            console.error('Error deleting customer:', error);
          });
      }
    },
    viewUserPurchases(userId) {
      this.loadingPurchases = true;
      this.showUserPurchases = true;
      
      axios.get(`/api/users/${userId}/purchases`)
        .then(response => {
          // Process purchase data to ensure it has all required fields
          this.userPurchases = response.data.map(purchase => {
            // Use purchase_products if available, or process products if not
            if (purchase.purchase_products && purchase.purchase_products.length > 0) {
              purchase.products = purchase.purchase_products.map(pp => {
                return {
                  product_id: pp.product_id,
                  quantity: pp.quantity,
                  unit_price: pp.unit_price,
                  // Add product name if available
                  product_name: pp.product ? pp.product.name : null
                };
              });
            } else if (purchase.products) {
              purchase.products = purchase.products.map(product => {
                return {
                  ...product,
                  unit_price: product.unit_price || product.price || 0
                };
              });
            }
            return purchase;
          });
          this.loadingPurchases = false;
        })
        .catch(error => {
          console.error('Error loading purchases:', error);
          this.loadingPurchases = false;
        });
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
    }
  }
}
</script>
