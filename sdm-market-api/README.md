# Sistema de Gerenciamento de Vendas

Este é um sistema simples de gerenciamento de vendas desenvolvido com Flask e SQLite, que permite o controle de clientes, produtos e compras.

## Estrutura do Projeto

```
app/
├── api/            # Endpoints da API REST
├── models/         # Modelos do banco de dados
├── schemas/        # Schemas para serialização
└── services/       # Lógica de negócio
```

## API Endpoints

### Clientes (Users)

- **POST /api/users**
  - Criar um novo cliente
  ```json
  {
    "name": "João Silva",
    "email": "joao@exemplo.com",
    "phone": "11999999999"
  }
  ```

- **GET /api/users**
  - Listar todos os clientes

- **GET /api/users/{id}**
  - Obter um cliente específico

- **PUT /api/users/{id}**
  - Atualizar um cliente
  ```json
  {
    "name": "João Silva Atualizado",
    "email": "joao.novo@exemplo.com",
    "phone": "11999999999"
  }
  ```

- **DELETE /api/users/{id}**
  - Remover um cliente

### Produtos (Products)

- **POST /api/products**
  - Criar um novo produto
  ```json
  {
    "name": "Produto Exemplo",
    "description": "Descrição do produto",
    "price": 99.99
  }
  ```

- **GET /api/products**
  - Listar todos os produtos

- **GET /api/products/{id}**
  - Obter um produto específico

- **PUT /api/products/{id}**
  - Atualizar um produto
  ```json
  {
    "name": "Produto Atualizado",
    "description": "Nova descrição",
    "price": 149.99
  }
  ```

- **DELETE /api/products/{id}**
  - Remover um produto

### Compras (Purchases)

- **POST /api/purchases**
  - Criar uma nova compra
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
  - Listar todas as compras

- **GET /api/purchases/{id}**
  - Obter uma compra específica

- **GET /api/users/{user_id}/purchases**
  - Listar compras de um cliente específico

- **DELETE /api/purchases/{id}**
  - Remover uma compra

## Regras de Negócio

1. **Usuários**
   - Nome, email e telefone são obrigatórios
   - Email deve ser único no sistema

2. **Produtos**
   - Nome e preço são obrigatórios
   - Preço deve ser maior que zero

3. **Compras**
   - Uma compra deve estar associada a um usuário existente
   - Uma compra deve ter pelo menos um produto
   - A quantidade de cada produto deve ser maior que zero
   - O preço unitário é registrado no momento da compra
   - O valor total é calculado automaticamente

## Como Executar

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o servidor:
```bash
flask run
```

O servidor estará disponível em `http://localhost:5000`

## Tecnologias Utilizadas

- Flask (Framework Web)
- SQLAlchemy (ORM)
- SQLite (Banco de Dados)
- Marshmallow (Serialização)
- Flask-CORS (Suporte a CORS)