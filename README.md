
### Get repo
```
git clone https://github.com/cardosorrenan/desafio-dev
```

# Config Install

## 1. Local
---
### 1.1 - Setup Database
---
#### 1.1.1 - Install postgres
```

```

#### 1.1.2 - Accessing postgres via command-line
```
sudo -i -u postgres

psql
```

#### 1.1.3 - Creating Database and User
```
CREATE DATABASE mylogbook;

CREATE USER mylogbook_user WITH ENCRYPTED PASSWORD 'mylogbook_pass';

GRANT ALL PRIVILEGES ON DATABASE mylogbook TO mylogbook;
```

#### 1.1.4 - User permit create database for tests
```
ALTER USER mylogbook_user CREATEDB;

exit;
```

### 1.2 - Setup Application
---
#### 1.2.1 - Open app folder after download repo
```
cd my_logbook
```

#### 1.2.2 - Install virtual environment (venv)
```
pip install virtuaenv
```

#### 1.2.3 - Create a venv 'env'
```
python -m venv env
```

#### 1.2.4 - Activate env
```
source env/bin/activate
```

#### 1.2.5 - Install packages
```
pip install -r requirements.txt
```

#### 1.2.6 - Create migrations
```
python manage.py makemigrations
```

#### 1.2.7 - Run migrate
```
python manage.py migrate
```

#### 1.2.8 - Create superuser (dev/tests purposes)
```
./manage.py create_superuser_test --username superuser_test --password 1234 --noinput --email 'superuser@test.com'
```

#### 1.2.9 - Dump data
```
python manage.py loaddata app/fixtures/*.json
```

#### 1.2.10 - Run tests
```
python manage.py test
```

#### 1.2.11 - Run app
```
python manage.py runserver
```

- http://localhost:8000


## 1.2 - Docker
---

#### 1.2.1 - Run docker compose gracefully
```
docker-compose up --build -d
```

- http://localhost:8000


# API Docs

## Insomnia File


## Relational diagram


## Routes

### File Uploads
### Stores
### Transactions