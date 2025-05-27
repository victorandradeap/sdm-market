# SDM Market System

This project contains a sales management system developed for the Distributed Systems course, featuring a Vue.js frontend and a Flask API backend.

## Overview

SDM Market demonstrates distributed systems principles through a sales management application. The system architecture follows a modern microservices approach with decoupled frontend and backend components communicating over HTTP. This architecture showcases key distributed systems concepts including:

- **Service Decoupling**: Separation of frontend and backend concerns
- **RESTful Communication**: Standard HTTP protocol for service communication
- **Containerization**: Docker-based deployment for consistent environment
- **Data Persistence**: Database management across service boundaries
- **Scalability**: Independent scaling of frontend and backend components

## Running with Docker Compose

The easiest way to run the application is using Docker Compose, which will start both frontend and backend services.

### Prerequisites

- Docker and Docker Compose installed on your machine
- Git for cloning the repository

### Steps to Run

1. Clone this repository
   ```bash
   git clone <repository-url>
   cd sdm-market
   ```

2. Start the application using Docker Compose
   ```bash
   docker-compose up -d
   ```

3. Access the application
   - Frontend: http://localhost:8080
   - API: http://localhost:5000

### Services

- **Frontend (sdm-market-page)**
  - Vue.js application running on port 8080
  - Container name: `sdm-market-page`
  - Uses NGINX as a web server

- **Backend API (sdm-market-api)**
  - Flask API running on port 5000
  - Container name: `sdm-market-api`
  - SQLite database stored in a persistent volume

## Project Structure

### Frontend (sdm-market-page)

The frontend is built with Vue.js and includes the following components:

- **App.vue**: Main application component
- **Users.vue**: Customer management interface
- **Products.vue**: Product management interface
- **Purchases.vue**: Purchase management interface

### Backend (sdm-market-api)

The backend follows a structured approach with:

- **Models**: Database entity definitions (User, Product, Purchase)
- **Services**: Business logic layer
- **Schemas**: Data serialization and validation
- **API Routes**: RESTful endpoints

## API Endpoints

The backend provides the following RESTful API endpoints:

- **/api/users**: User management
- **/api/products**: Product management
- **/api/purchases**: Purchase management

## Development

To develop the application locally:

1. Start the services in development mode
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
   ```

2. Access the logs for debugging
   ```bash
   docker-compose logs -f
   ```

## Troubleshooting

If you encounter issues:

1. Check the container logs
   ```bash
   docker-compose logs api
   docker-compose logs frontend
   ```

2. Restart the services
   ```bash
   docker-compose restart
   ```
