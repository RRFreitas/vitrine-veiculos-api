# Teste Prático Full Stack Python (Backend)

### Tecnologias utilizadas no Backend:
- Django
- Django Rest Framework
- Django Simple JWT
- PostgreSQL 11
- Docker (Opcional)
- Pipenv (Opcional)

### Casos de uso:
- Listagem, criação, edição e remoção de veículos
- Login com token JWT
- Rotas de listagens públicas
- Rotas de criação, edição e remoção privadas (necessária autenticação com JWT)

### Para rodar o projeto é preciso:
- Python
- Docker

### Instalando o projeto
```shell
# Clone o repositório
$ git clone https://github.com/RRFreitas/vitrine-veiculos-api.git

# Acesse o diretório do projeto
$ cd vitrine-veiculos-api

# Ative seu virtualenv (opcional)
$ pipenv shell

# Instale os requisitos
$ pip install -r requirements.txt
```

### Configuração
No arquivo .env altere as variáveis de configuração de acordo com sua preferência:
```shell
POSTGRES_HOST = '127.0.0.1'
POSTGRES_PORT = '5432'
DATABASE = 'postgres'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '1234'
PORT = '8000'
SECRET_KEY = 'django-insecure-secret-key-329fjnalc'
DEBUG = 'True'
```

### Preparando o banco de dados
É necessário um banco postgres, você pode subir um banco local facilmente com o docker:
```shell
# Baixando imagem docker
$ docker pull postgres

# Rodando container com porta 5432 e senha 1234
$ docker run -p 5432:5432 -v /tmp/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres
```
Agora, aplique as migrations no banco:
```shell
$ python manage.py migrate
```
Crie um admin:
```shell
$ python manage.py createsuperuser
```

### Rodando os testes
```shell
$ python manage.py test
```

### Rodando o servidor
```shell
$ python manage.py runserver
```

Pronto! Agora siga para rodar o [frontend](https://github.com/RRFreitas/vitrine-veiculos-frontend)

## Endpoints

### /token/ (POST)
Endpoint de autenticação, é enviado login e senha e retornado dois tokens, um de access e outro de refresh, o de refresh tem maior duração e serve para pedir outro token de acesso
#### Exemplo de body
```json
{
  "username": "admin",
  "password": "admin123"
}
```
#### Retorno
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

### /token/refresh/ (POST)
Endpoint para pedir um novo token de acesso, é enviado um token de refresh válido e é retornado um novo token de acesso e refresh.
#### Exemplo de body
```json
{
  "refresh" : "REFRESH_TOKEN"
}
```
#### Retorno
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

### /carros/ (GET)
Endpoint público de listagem de carros, não é necessário o envio de token.
#### Retorno
```json
[{
    "id": 1,
    "nome":"Uno",
    "marca":"Fiat",
    "ano":2020,
    "km":1300,
    "estado":"SP",
    "valor":30000,
    "foto":"https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
}]
```

### /carros/{id}/ (POST)
Endpoint privado de inserção de carros, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
    "nome":"Uno",
    "marca":"Fiat",
    "ano":2020,
    "km":1300,
    "estado":"SP",
    "valor":30000,
    "foto":"https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
}
```

### /carros/{id}/ (PUT)
Endpoint privado de edição de carros, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
    "nome":"Mobi",
    "marca":"Fiat",
    "ano":2023,
    "km":2300,
    "estado":"PB",
    "valor":70000,
    "foto":"https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
}
```

### /carros/{id} (DELETE)
Endpoint privado de deleção de carros, é necessário o envio de token JWT no header Authorization.
