# Sistema SDM Market

Este projeto contém um sistema de gerenciamento de vendas composto por um frontend em Vue.js e um backend em Flask API.

## Executando com Docker Compose

A maneira mais fácil de executar a aplicação é usando Docker Compose, que iniciará tanto os serviços de frontend quanto de backend.

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina

### Passos para executar

1. Clone este repositório
   ```bash
   git clone <url-do-repositório>
   cd sdm-market
   ```

2. Inicie a aplicação usando Docker Compose
   ```bash
   docker-compose up -d
   ```

3. Acesse a aplicação
   - Frontend: http://localhost:8080
   - API: http://localhost:5000

### Serviços

- **Frontend (sdm-market-page)**
  - Aplicação Vue.js rodando na porta 8080
  - Nome do container: `sdm-market-page`

- **Backend API (sdm-market-api)**
  - API Flask rodando na porta 5000
  - Nome do container: `sdm-market-api`
  - Banco de dados SQLite armazenado em um volume persistente
