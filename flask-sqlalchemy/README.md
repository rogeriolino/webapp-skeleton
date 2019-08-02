# Flask SQLAlchemy

Esqueleto de aplicação Python Flask com SQLAlchemy configurado.

## Requisitos

- Python3
- MySQL 5.7


## Instalação

Instalação global:

    pip install -r requirements.txt

Ou apenas para o usuário atual:

    pip install -r requirements.txt --user


## Banco de dados

Criação do banco MySQL

    CREATE DATABASE `flask_sqlalchemy`;
    USE `flask_sqlalchemy`;

    Create TABLE `todos` (
        `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `title` VARCHAR(80) NOT NULL,
        `text` TEXT NULL,
        `done` BOOLEAN NOT NULL DEFAULT FALSE,
        `pub_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    INSERT INTO `todos` (`title`, `text`) VALUES ('Homework', 'My beautiful homework');

## Executando

Exportar a varíavel de ambiente `DATABASE_URI` com a URI de conexão com o banco e executar o script python3 app.py.

    export DATABASE_URI=mysql+pymysql://user:pass@host:3306/dbname
    python3 src/app.py

Ou

    DATABASE_URI=mysql+pymysql://user:pass@host:3306/dbname python3 src/app.py


**OBS**: A aplicação roda por padrão na porta `5000`.


## Uso

Inserir novo TODO

    curl -H "Content-type: application/json" -d '{"title": "New TODO", "text": "inserting new TODO via curl"}' 'http://127.0.0.1:5000/'



## Docker

Build

    docker build -t flask_sqlalchemy:latest .

Run

    docker run \
        -it --rm \
        -p 5000:5000 \
        -e DATABASE_URI=mysql+pymysql://user:pass@host:3306/dbname \
        --name flask_sqlalchemy \
        flask_sqlalchemy:latest