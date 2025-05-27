# Sales Management System API

This is a backend service for the SDM Market distributed system, developed with Flask and SQLite for the Distributed Systems course. The API provides endpoints for managing customers, products, and purchases in a microservices architecture.

## Distributed Systems Architecture

This API component serves as the backend microservice in the SDM Market distributed system. It demonstrates several key distributed systems concepts:

1. **REST API**: Provides stateless communication through HTTP endpoints
2. **Data Persistence**: Manages consistent data storage for the entire system
3. **Service Independence**: Operates as a standalone service with clear boundaries
4. **API Contract**: Defines a stable interface for frontend communication
5. **Stateless Processing**: Each request contains all necessary information

## Project Structure

```
app/
├── api/            # REST API endpoints
├── models/         # Database models
├── schemas/        # Serialization schemas
└── services/       # Business logic
```

## API Endpoints

### Users

- **POST /api/users**
  - Create a new customer
  ```json
  {
    "name": "John Smith",
    "email": "john@example.com",
    "phone": "11999999999"
  }
  ```

- **GET /api/users**
  - List all customers

- **GET /api/users/{id}**
  - Get a specific customer

- **PUT /api/users/{id}**
  - Update a customer
  ```json
  {
    "name": "John Smith Updated",
    "email": "john.new@example.com",
    "phone": "11999999999"
  }
  ```

- **DELETE /api/users/{id}**
  - Remove a customer

### Products

- **POST /api/products**
  - Create a new product
  ```json
  {
    "name": "Example Product",
    "description": "Product description",
    "price": 99.99
  }
  ```

- **GET /api/products**
  - List all products

- **GET /api/products/{id}**
  - Get a specific product

- **PUT /api/products/{id}**
  - Update a product
  ```json
  {
    "name": "Updated Product",
    "description": "New description",
    "price": 149.99
  }
  ```

- **DELETE /api/products/{id}**
  - Remove a product

### Purchases

- **POST /api/purchases**
  - Create a new purchase
  ```json
  {
    "user_id": 1,
    "products": [
      {
        "product_id": 1,
        "quantity": 2
      },
      {
        "product_id": 2,
        "quantity": 1
      }
    ]
  }
  ```

- **GET /api/purchases**
  - List all purchases

- **GET /api/purchases/{id}**
  - Get a specific purchase

- **GET /api/users/{user_id}/purchases**
  - List purchases for a specific customer

- **DELETE /api/purchases/{id}**
  - Remove a purchase

## Business Rules

1. **Users**
   - Name, email, and phone are required
   - Email must be unique in the system

2. **Products**
   - Name and price are required
   - Price must be greater than zero

3. **Purchases**
   - A purchase must be associated with an existing user
   - A purchase must have at least one product
   - The quantity of each product must be greater than zero
   - The unit price is recorded at the time of purchase
   - The total value is calculated automatically

## Distributed Systems Considerations

### 1. Data Consistency
The API ensures data consistency by implementing transaction management for operations that affect multiple entities (e.g., creating a purchase that affects product inventory).

### 2. API Versioning
The API structure supports versioning to allow for future changes while maintaining backward compatibility.

### 3. Error Handling
Standardized error responses are implemented to provide clear feedback to distributed clients:
- 400: Bad Request - Invalid input data
- 404: Not Found - Resource doesn't exist
- 409: Conflict - Business rule violation
- 500: Internal Server Error - Unexpected errors

### 4. Scalability
The stateless design allows for horizontal scaling by deploying multiple instances behind a load balancer.

## Running the Service

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
flask run
```

The server will be available at `http://localhost:5000`

## Technologies Used

- **Flask**: Web framework for building RESTful APIs
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Database for persistent storage
- **Marshmallow**: Serialization/deserialization and validation
- **Flask-CORS**: Cross-Origin Resource Sharing support for distributed frontends

## Performance Metrics

When evaluating this backend service in a distributed environment, consider these metrics:

- **Response Time**: Average time to process API requests
- **Throughput**: Number of requests handled per second
- **Error Rate**: Percentage of failed requests
- **Resource Utilization**: CPU, memory, and I/O usage under load