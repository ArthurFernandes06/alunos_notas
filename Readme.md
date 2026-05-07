# API para cadastro de alunos e Notas

API REST desenvolvida com FastAPI para gerenciamento de alunos, provas e notas.

## Tecnologias

- Python
- FastAPI
- MySQL
- Pydantic
- Docker

---

# Base URL

```text
http://localhost:8000
```

---

# Documentação Interativa

## Swagger UI

```text
http://localhost:8000/docs
```

## ReDoc

```text
http://localhost:8000/redoc
```

# Como executar

## Clonar repositório

```bash
git clone https://github.com/ArthurFernandes06/alunos_notas.git
```

## Entrar na pasta

```bash
cd alunos_notas
```

## Executar containers

```bash
docker compose up --build
```

## Observações
A aplicação roda por padrão a api na porta 8000 e o mysql na porta 3306, essas portas tem que estar disponíveis na sua máquina. Caso não esteja pare de rodar, ou altere no arquivo .env na raiz do projeto o APP_PORT e o MYSQL_PORT.