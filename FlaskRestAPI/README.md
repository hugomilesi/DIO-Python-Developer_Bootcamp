# Python Flask RestAPI

## **Descrição:**
Este projeto é uma API de streaming de música desenvolvida usando o framework Flask em Python. A API permite que os usuários obtenham informações sobre artistas musicais e também interajam com a plataforma para adicionar, atualizar e excluir artistas. A API é construída usando a extensão Flask-RESTful, que facilita a criação de endpoints de API RESTful.

---
## Etapas do Projeto
- Criação do Esquema relacional com SQLAlchemy.
- Inserção de dados.
- Recuperação de dados(queries).
- Integração com o banco de dados através da biblioteca flask_restful.
- Criação das rotas e do CRUD.

## Recursos
- **User Endpoint:** Este endpoint permite aos usuários obter informações sobre um usuário específico fornecendo o nome como parâmetro. As informações incluem nome, sobrenome, email e endereço.
- **Artist Endpoint:** Este endpoint permite aos usuários obter informações detalhadas sobre um artista específico por meio do nome como parâmetro. Além disso, ele permite atualizar informações do artista ou excluí-lo.
- **ListArtists Endpoint:** Este endpoint fornece uma lista de todos os artistas presentes na plataforma, bem como a capacidade de adicionar novos artistas.
---

## Tecnologias Utulizadas
- **Flask:** O projeto foi construído usando o framework Flask, que é conhecido por sua simplicidade e flexibilidade no desenvolvimento de aplicativos web.
- **Flask-RESTful:** A extensão Flask-RESTful é utilizada para criar endpoints de API RESTful de forma organizada e eficiente.
- **SQLite:** O banco de dados SQLite é usado para armazenar informações sobre usuários e artistas, permitindo a persistência dos dados.
- **SQLAlchemy:** A biblioteca SQLAlchemy é usada para interagir com o banco de dados e realizar operações como consultas, atualizações e exclusões.
- **JSON:** As informações da API são trocadas no formato JSON, que é comum em serviços web.
---

## Execução:
Para executar o projeto, basta executar o arquivo principal (app.py) após ter configurado o ambiente Python. A aplicação será iniciada em modo de depuração, permitindo o teste e desenvolvimento local.

Este é um projeto interessante que demonstra habilidades em criação de API usando Flask, interação com banco de dados e implementação de operações CRUD (Create, Read, Update, Delete) em um contexto de streaming de música.
