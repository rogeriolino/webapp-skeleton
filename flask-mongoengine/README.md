# Flask MongoEngine

Esqueleto de aplicação Python Flask com MongoEngine configurado.

## Requisitos

- Python3
- MongoDB 3


## Instalação

Instalação global:

    pip install -r requirements.txt

Ou apenas para o usuário atual:

    pip install -r requirements.txt --user


## Executando

Exportar a varíavel de ambiente `DATABASE_URI` com a URI de conexão com o banco e executar o script python3 app.py.

    export DATABASE_URI=mongodb://user:pass@host:27017/dbname?authSource=admin
    python3 src/app.py

Ou

    DATABASE_URI=mongodb://user:pass@host:27017/dbname?authSource=admin python3 src/app.py


**OBS**: A aplicação roda por padrão na porta `5000`.


## Uso

Inserir novo TODO

    curl -H "Content-type: application/json" -d '{"title": "New TODO", "text": "inserting new TODO via curl"}' 'http://127.0.0.1:5000/'



## Docker

Build

    docker build -t flask_mongoengine:latest .

Run

    docker run \
        -it --rm \
        -p 5000:5000 \
        -e DATABASE_URI=mongodb://user:pass@host:27017/dbname?authSource=admin python3 src/app.py \
        --name flask_mongoengine \
        flask_mongoengine:latest