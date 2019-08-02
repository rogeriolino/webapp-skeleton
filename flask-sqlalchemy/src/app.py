import json
from flask import Flask, request, abort
import os
from waitress import serve
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db.init_app(app)

@app.route("/", methods=['GET'])
def get_collection():
    todos = Todo.query.all()
    resp = list(map(lambda t: t.as_dict(), todos))
    return json.dumps(resp), 200

@app.route('/', methods=['POST'])
def add_collection_item():
    content = request.get_json(silent=True)
    todo = Todo(content['title'], content['text'])
    db.session.add(todo)
    db.session.commit()
    resp = todo.as_dict()
    return json.dumps(resp), 200

@app.route("/<int:id>", methods=['GET'])
def get_item(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo is None:
        return abort(404)
    resp = todo.as_dict()
    return json.dumps(resp), 200

@app.route('/<int:id>', methods=['PUT'])
def update_item(id):
    # TODO
    pass

@app.route('/<int:id>', methods=['DELETE'])
def delete_item(id):
    # TODO
    pass


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)