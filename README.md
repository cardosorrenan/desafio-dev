
# My Log Book

<p align="center">
  <img width="500" src="./assets/screen.png">
</p>

---

<h6 align="center">
An app for tracking financial transactions :moneybag:
</h6>

### Get repo
```
git clone https://github.com/cardosorrenan/desafio-dev
```
####
```
cd desafio_dev/my_logbook/
```

# Installation steps

## 1º Option - Docker :rocket:

#### 1.1 - Run docker compose
```
docker-compose up --build -d
```

#### 1.2 - Go to app :desktop_computer:
- Upload the CNAB file at http://localhost:8000/upload_cnab
- Check your transactions at http://localhost:8000

## 2º Option - Prepare the local environment :inbox_tray:

#### Pre-requirements :wrench:

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Postgres](https://www.postgresql.org/download/)

### 2.1 - Setup Database :abacus:
---

#### 2.1.1 - Accessing postgres via command-line
```
sudo service postgresql start

sudo -i -u postgres

psql
```

#### 2.1.2 - Creating database and user
```
CREATE DATABASE mylogbook;

CREATE USER mylogbook_user WITH ENCRYPTED PASSWORD 'mylogbook_pass';

GRANT ALL PRIVILEGES ON DATABASE mylogbook TO mylogbook_user;
```

#### 2.1.3 - User permit create database for tests
```
ALTER USER mylogbook_user CREATEDB;

exit;
```

### 2.2 - Setup Application :desktop_computer:
---

#### 2.2.1 - Install virtual environment (venv)
```
pip3 install virtualenv
```

#### 2.2.2 - Create a venv 'env'
```
python3 -m venv env
```

#### 2.2.3 - Activate env
```
source env/bin/activate
```

#### 2.2.4 - Install packages
```
pip3 install -r requirements.txt
```

#### 2.2.5 - Create migrations
```
python3 manage.py makemigrations
```

#### 2.2.6 - Run migrate
```
python3 manage.py migrate
```

#### 2.2.7 - Create superuser (dev/tests purposes)
```
./manage.py create_superuser_test --username superuser_test --password 1234 --noinput --email 'superuser@test.com'
```

#### 2.2.8 - Dump data
```
python3 manage.py loaddata app/fixtures/*.json
```
- Transaction types and a predefined OAuth application provider

#### 2.2.9 - Run tests
```
python3 manage.py test
```

#### 2.2.10 - Run app
```
python3 manage.py runserver
```

#### 2.2.11 - Go to app
- Upload the CNAB file at http://localhost:8000/upload_cnab
- Check your transactions at http://localhost:8000


# API Docs :scroll:

### Insomnia File
---
<a href="./assets/Insomnia_2022-01-18.json" download>Click to Download</a>

### Relational diagram
---
<p align="center">
  <img width="400" src="./assets/dr.png">
</p>

### Oauth
---

#### GET: /o/token
```
REQUEST
{
    "client_secret": "client_secret_test", 
    "client_id": "client_id_test", 
    "grant_type": "password",
    "username": "superuser_test", 
    "password": "1234"
}

RESPONSE
{
  "access_token": "wS4W3gUdlL2KdMcCQHQBf7W0pTO4sR",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "jUsEidWSHx2lWSKnCZkZ9juAWsWmxy"
}
```

#### GET: /o/revoke_token
```
REQUEST
{
	"client_secret": "client_secret_test", 
	"client_id": "client_id_test", 
	"token": "wS4W3gUdlL2KdMcCQHQBf7W0pTO4sR"
}

RESPONSE
200
```

- Obs.: Use token authorization on every request
```
Authorization: Bearer <token>
```

### Store
---
```
 Store {
    name: string
    owner: string
 }
 ```

 | | URL | METHOD | BODY | RESPONSE |
 | :-: | :-: | :-: | :-: | :-: |
 | INDEX | /api/v1/store | GET | - | Store[ ] |
 | GET ONE | /api/v1/store/{id} | GET | - | Store |
 | GET AMOUNT | /api/v1/store/{id}/amount | GET | - | id,<br /> amount |
 | CREATE | /api/v1/store | POST | Store | Store |
 | EDIT | /api/v1/store/{id} | PATCH | Store | Store |
 | DELETE | /api/v1/store/{id} | DELETE | - | - |


### Transaction
---
```
 Transaction {
    file_origin = int
    type = int
    store = int
    datetime = datetime
    value = decimal
    cpf = string
    card = string
 }
 ```

 | | URL | METHOD | BODY | RESPONSE |
 | :-: | :-: | :-: | :-: | :-: |
 | INDEX | /api/v1/transaction | GET | - | Transaction[ ] |
 | GET ONE | /api/v1/transaction/{id} | GET | - | Transaction |
 | CREATE | /api/v1/transaction | POST | Transaction | Transaction |
 | EDIT | /api/v1/transaction/{id} | PATCH | Transaction | Transaction |
 | DELETE | /api/v1/transaction/{id} | DELETE | - | - |

### File Origin (Uploads)
---
```
 FileOrigin {
    filename = string
    content_type = string
    size = float
    entries = int
    created_at = datetime
    updated_at = datetime
 }
 
 
 ```

 | | URL | METHOD | BODY | RESPONSE |
 | :-: | :-: | :-: | :-: | :-: |
 | INDEX | /api/v1/file_origin | GET | - | FileOrigin[ ] |
 | GET ONE | /api/v1/file_origin/{id} | GET | - | FileOrigin |
