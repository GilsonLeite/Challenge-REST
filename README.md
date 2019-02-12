# API REST Framework

# Especificações e Requisitos do Projeto
Desenvolvimento de um projeto Django e DRF com implementação CRUD, relacionamento one-to-many e autenticação para consumo de dados.

#### APP Teacher:
- Nome

#### APP Student:
- Nome

#### API REST deve efetuar as seguintes interações
- Lista de Professores
- Detalhes de um professor
- Cadastro de um professor
- Atualização de um professor
- Exclusão de um professor

- Lista de alunos com o professor relacionado
- Detalhes de aluno com o professor relacionado
- Cadastro de aluno com o professor relacionado
- Atualização aluno com o professor relacionado
- Exclusão de aluno com o professor relacionado


## Tecnologias
Django framework versão 2.0.10,

Django REST Framework versão 3.9.1,

Linguagem de programação Python 3.6.5,

Banco de dados Sqlite3.


## Instalação

**1. Download do projeto via git clone**:

`$ git clone https://github.com/GilsonLeite/Challenge-REST.git`

**2. Acesse o projeto e crie o ambiente virtual**:

`$ cd Challenge-REST`

`python3 -m venv venv`

`mkdir venv`

`.venv/bin/activate`

**3. Instalando as dependencias:**

`(venv)$ pip install -r requirements.txt`

**4. Criando o banco de dados e usuario:**

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

**5. Executando o projeto:**
`python manage.py runserver`


**6. Acessando API Root**
http://127.0.0.1:8000/api/v1/



### Endpoints
**Método**|**URL**|**Ação**
:--:|:--:|:--:
GET|`http://127.0.0.1:8000/api/v1/teacher/`|lista os professores
GET|`http://127.0.0.1:8000/api/v1/teacher/<id>`|Detalhe do professores
POST|`http://127.0.0.1:8000/api/v1/teacher/`|cria um novo professor
PUT|`http://127.0.0.1:8000/api/v1/teacher/<id>/`|atualiza um professor
DELETE|`http://127.0.0.1:8000/api/v1/teacher/<id>/`|deleta um professor

**Estrutura Professor**
```json
[
    {
        "name": "Gilson",
        "resource_uri": "/api/v1/teacher/1/",
        "id": 1
    }
]
```

### Endpoints
**Método**|**URL**|**Ação**
:--:|:--:|:--:
GET|`http://127.0.0.1:8000/api/v1/student/`|lista os alunos
GET|`http://127.0.0.1:8000/api/v1/student/<id>`|Detalhe do aluno
POST|`http://127.0.0.1:8000/api/v1/student/`|cria um novo aluno
PUT|`http://127.0.0.1:8000/api/v1/student/<id>/`|atualiza um aluno
DELETE|`http://127.0.0.1:8000/api/v1/student/<id>/`|deleta um aluno


**Estrutura Aluno**
```json
[
    {
        "name": "Lucas",
        "id": 39,
        "resource_uri": "/api/v1/student/39/",
        "teacher": {
            "name": "Gilson",
            "resource_uri": "/api/v1/teacher/1/",
            "id": 1
        }
    }
 ]

```