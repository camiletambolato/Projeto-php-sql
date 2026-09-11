API REST simples desenvolvida em **PHP** para gerenciamento e inserção de produtos em um banco de dados **PostgreSQL**, com testes realizados via extensão **Thunder Client** no VS Code.

---

##  Tecnologias Utilizadas

- **Linguagem:** PHP 8.x
- **Banco de Dados:** PostgreSQL
- **Cliente HTTP:** Thunder Client (Extensão para VS Code)
- **Servidor Local:** PHP Built-in Web Server

---

##  Estrutura do Projeto

```text
Projeto-produtos/
├── .gitignore
├── conexao.php      # Arquivo de configuração da conexão PDO com o PostgreSQL
├── produtos.php     # Endpoint para operações de GET e POST
├── teste.py         # Script auxiliar/automação em Python
└── README.md        # Documentação do projeto
⚙️ Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

PHP (versão 8.0 ou superior) com o driver pdo_pgsql habilitado.

PostgreSQL instalado e em execução.

Visual Studio Code com a extensão Thunder Client.

 Como Executar o Projeto
1. Configurar o Banco de Dados
Acesse seu gerenciador do PostgreSQL (pgAdmin, DBeaver ou terminal psql) e crie o banco de dados e a tabela:

SQL
-- Criar o banco de dados
CREATE DATABASE projeto_produtos;

-- Criar a tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);
2. Configurar o Arquivo conexao.php
Ajuste os dados de conexão de acordo com as configurações da sua máquina:

PHP
<?php
$host = 'localhost';
$port = '5432'; // Ajuste caso sua porta seja diferente (ex: 5438)$dbname = 'projeto_produtos';
$user = 'postgres';$password = 'sua_senha';

try {
    $pdo = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $user, $password);$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erro na conexão: " . $e->getMessage());
}
?>
3. Iniciar o Servidor PHP
Abra o terminal na pasta raiz do projeto (Projeto-produtos) e rode o servidor embutido do PHP:

Bash
php -S localhost:8000
 Testando as Requisições no Thunder Client
Com o servidor rodando em http://localhost:8000, utilize a extensão Thunder Client no VS Code:

1. Adicionar/Cadastrar Produto (POST)
Método: POST

URL: http://localhost:8000/produtos.php

Query Parameters: (deixe totalmente vazio)

Body: Selecione JSON e insira o corpo da requisição:

JSON
{
    "nome": "Notebook",
    "preco": 3500
}
Exemplo de Resposta (201 Created):
JSON
{
    "mensagem": "Produto cadastrado com sucesso!",
    "id": 1
}
2. Listar Produtos (GET)
Método: GET

URL: http://localhost:8000/produtos.php

Exemplo de Resposta (200 OK):
JSON
[
  {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500.00
  },
  {
    "id": 2,
    "nome": "Mouse",
    "preco": 80.00
  }
]
 Erros Comuns e Soluções
Problema / Mensagem	Causa	Solução
Connection refused	O PostgreSQL não está rodando ou a porta no conexao.php está errada.	Verifique se o serviço do PostgreSQL está iniciado e confirme se a porta é 5432 ou 5438.
Driver not found	A extensão PDO do PostgreSQL não está ativada no PHP.	Edite seu arquivo php.ini e descomente a linha extension=pdo_pgsql.
 Autor
Desenvolvido por Camile Tambolato

Estudante de Técnico em Desenvolvimento de Sistemas - SENAI

quero o arquivo para baixar

 Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

PHP (versão 8.0 ou superior) com o driver pdo_pgsql habilitado.

PostgreSQL instalado e em execução.

Visual Studio Code com a extensão Thunder Client.

 Como Executar o Projeto
1. Configurar o Banco de Dados
Acesse seu gerenciador do PostgreSQL (pgAdmin, DBeaver ou terminal psql) e crie o banco de dados e a tabela:

SQL
-- Criar o banco de dados
CREATE DATABASE projeto_produtos;

-- Criar a tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);
2. Configurar o Arquivo conexao.php
Ajuste os dados de conexão de acordo com as configurações da sua máquina:

PHP
<?php
$host = 'localhost';
$port = '5432'; // Ajuste caso sua porta seja diferente (ex: 5438)$dbname = 'projeto_produtos';
$user = 'postgres';$password = 'sua_senha';

try {
    $pdo = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $user, $password);$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erro na conexão: " . $e->getMessage());
}
?>
3. Iniciar o Servidor PHP
Abra o terminal na pasta raiz do projeto (Projeto-produtos) e rode o servidor embutido do PHP:

Bash
php -S localhost:8000
 Testando as Requisições no Thunder Client
Com o servidor rodando em http://localhost:8000, utilize a extensão Thunder Client no VS Code:

1. Adicionar/Cadastrar Produto (POST)
Método: POST

URL: http://localhost:8000/produtos.php

Query Parameters: (deixe totalmente vazio)

Body: Selecione JSON e insira o corpo da requisição:

JSON
{
    "nome": "Notebook",
    "preco": 3500
}
Exemplo de Resposta (201 Created):
JSON
{
    "mensagem": "Produto cadastrado com sucesso!",
    "id": 1
}
2. Listar Produtos (GET)
Método: GET

URL: http://localhost:8000/produtos.php

Exemplo de Resposta (200 OK):
JSON
[
  {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500.00
  },
  {
    "id": 2,
    "nome": "Mouse",
    "preco": 80.00
  }
]
 Erros Comuns e Soluções
Problema / Mensagem	Causa	Solução
Connection refused	O PostgreSQL não está rodando ou a porta no conexao.php está errada.	Verifique se o serviço do PostgreSQL está iniciado e confirme se a porta é 5432 ou 5438.
Driver not found	A extensão PDO do PostgreSQL não está ativada no PHP.	Edite seu arquivo php.ini e descomente a linha extension=pdo_pgsql.
 Autor
Desenvolvido por Camile Tambolato

Estudante de Técnico em Desenvolvimento de Sistemas - SENAI
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("Arquivo README.md gerado com sucesso!")


```text?code_stdout&code_event_index=1
Arquivo README.md gerado com sucesso!

Seu arquivo README.md está pronto para baixar!

Ícone do app MD
README
 MD 
Basta clicar no botão/link acima para fazer o download do arquivo .md e colocá-lo na pasta do seu projeto.




O Gemini é uma IA e pode cometer erros.

Analisando
# API REST de Produtos (PHP + PostgreSQL)

API REST simples desenvolvida em **PHP** para gerenciamento e inserção de produtos em um banco de dados **PostgreSQL**, com testes realizados via extensão **Thunder Client** no VS Code.

---

##  Tecnologias Utilizadas

- **Linguagem:** PHP 8.x
- **Banco de Dados:** PostgreSQL
- **Cliente HTTP:** Thunder Client (Extensão para VS Code)
- **Servidor Local:** PHP Built-in Web Server

---

##  Estrutura do Projeto

```text
Projeto-produtos/
├── .gitignore
├── conexao.php      # Arquivo de configuração da conexão PDO com o PostgreSQL
├── produtos.php     # Endpoint para operações de GET e POST
├── teste.py         # Script auxiliar/automação em Python
└── README.md        # Documentação do projeto
```

---

##  Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:
1. **PHP** (versão 8.0 ou superior) com o driver `pdo_pgsql` habilitado.
2. **PostgreSQL** instalado e em execução.
3. **Visual Studio Code** com a extensão **Thunder Client**.

---

##  Como Executar o Projeto

### 1. Configurar o Banco de Dados
Acesse seu gerenciador do PostgreSQL (pgAdmin, DBeaver ou terminal `psql`) e crie o banco de dados e a tabela:

```sql
-- Criar o banco de dados
CREATE DATABASE projeto_produtos;

-- Criar a tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);
```

### 2. Configurar o Arquivo `conexao.php`
Ajuste os dados de conexão de acordo com as configurações da sua máquina:

```php
<?php
$host = 'localhost';
$port = '5432'; // Ajuste caso sua porta seja diferente (ex: 5438)
$dbname = 'projeto_produtos';
$user = 'postgres';
$password = 'sua_senha';

try {
    $pdo = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erro na conexão: " . $e->getMessage());
}
?>
```

### 3. Iniciar o Servidor PHP
Abra o terminal na pasta raiz do projeto (`Projeto-produtos`) e rode o servidor embutido do PHP:

```bash
php -S localhost:8000
```

---

##  Testando as Requisições no Thunder Client

Com o servidor rodando em `http://localhost:8000`, utilize a extensão **Thunder Client** no VS Code:

### 1. Adicionar/Cadastrar Produto (POST)
- **Método:** `POST`
- **URL:** `http://localhost:8000/produtos.php`
- **Query Parameters:** *(deixe totalmente vazio)*
- **Body:** Selecione **JSON** e insira o corpo da requisição:

```json
{
    "nome": "Notebook",
    "preco": 3500
}
```

#### Exemplo de Resposta (201 Created):
```json
{
    "mensagem": "Produto cadastrado com sucesso!",
    "id": 1
}
```

---

### 2. Listar Produtos (GET)
- **Método:** `GET`
- **URL:** `http://localhost:8000/produtos.php`

#### Exemplo de Resposta (200 OK):
```json
[
  {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500.00
  },
  {
    "id": 2,
    "nome": "Mouse",
    "preco": 80.00
  }
]
```

---

##  Erros Comuns e Soluções

| Problema / Mensagem | Causa | Solução |
| :--- | :--- | :--- |
| `Connection refused` | O PostgreSQL não está rodando ou a porta no `conexao.php` está errada. | Verifique se o serviço do PostgreSQL está iniciado e confirme se a porta é `5432` ou `5438`. |
| `Driver not found` | A extensão PDO do PostgreSQL não está ativada no PHP. | Edite seu arquivo `php.ini` e descomente a linha `extension=pdo_pgsql`. |

---

##  Autor

Desenvolvido por **Camile Tambolato**  
Estudante de Técnico em Desenvolvimento de Sistemas - SENAI
README.md
Exibindo README.md.