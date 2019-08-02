import json
from flask import Flask, request, abort
import os
from waitress import serve
from models import *

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'connect': False,
    'host': os.environ['DATABASE_URI']
}
app.app_context().push()

db.init_app(app)

@app.route("/", methods=['GET'])
def get_collection():
    # Todo.objects.paginate(page=page, per_page=10)
    todos = Todo.objects.all()
    resp = list(map(lambda t: t.as_dict(), todos))
    return json.dumps(resp), 200

@app.route('/', methods=['POST'])
def add_collection_item():
    content = request.get_json(silent=True)
    todo = Todo(title=content['title'], text=content['text'])
    todo.save()
    resp = todo.as_dict()
    return json.dumps(resp), 200

@app.route("/<id>", methods=['GET'])
def get_item(id):
    todo = Todo.objects.get_or_404(id=id)
    resp = todo.as_dict()
    return json.dumps(resp), 200

@app.route('/<id>', methods=['PUT'])
def update_item(id):
    # TODO
    pass

@app.route('/<id>', methods=['DELETE'])
def delete_item(id):
    # TODO
    pass


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)