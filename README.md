# SDM Market System

This project contains a sales management system composed of a Vue.js frontend and a Flask API backend.

## Running with Docker Compose

The easiest way to run the application is using Docker Compose, which will start both the frontend and backend services.

### Prerequisites

- Docker and Docker Compose installed on your machine

### Steps to run

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

- **Backend API (sdm-market-api)**
  - Flask API running on port 5000
  - Container name: `sdm-market-api`
  - SQLite database stored in a persistent volume

## Development
