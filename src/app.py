from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def todos_list():
    json_text = jsonify(todos)
    return json_text #The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list (todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data # { "done": true, "label": "Sample Todo 2" }
    decoded_object = json.loads(request_body) #Para decodificar cualquier string json y convertirlo a un objeto de python podemos usar esta función
    #también se podría hacer con request.json
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos) #REST APIs have to return data in JSON format

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)