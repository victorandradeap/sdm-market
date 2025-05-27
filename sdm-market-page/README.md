# SDM Market Frontend

This is the frontend component of the SDM Market distributed system, developed with Vue.js for the Distributed Systems course.

## Distributed Systems Architecture

This frontend component demonstrates key distributed systems concepts:

1. **Client-Server Communication**: Consumes REST API endpoints from the backend
2. **Decoupled UI Layer**: Separation of presentation from business logic
3. **Proxy Configuration**: Routes API requests through NGINX

## Project Structure

```
sdm-market-page/
├── src/
│   ├── components/   # Vue components (Users, Products, Purchases)
│   ├── App.vue       # Main application component
│   └── main.js       # Application entry point
├── Dockerfile        # Docker configuration
└── nginx.conf        # NGINX reverse proxy configuration
```

## UI Components

- **Users**: Customer management interface
- **Products**: Product catalog management
- **Purchases**: Order processing and history

## Distributed Systems Features

### Frontend-Backend Communication
```javascript
// Example API call
axios.get('/api/users')
  .then(response => this.users = response.data)
  .catch(error => console.error('Error:', error));
```

### Proxy Configuration
```
location /api/ {
    proxy_pass http://api:5000;
}
```

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run serve
```

## Technologies

- **Vue.js**: Frontend framework
- **Axios**: HTTP client
- **NGINX**: Web server and reverse proxy
- **Docker**: Containerization
