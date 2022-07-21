from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/hello', methods=['GET'])
def hello_world():
    return "<h1>Hello!</h1>"

@app.route('/todos', methods=['GET'])
def todos_list():
    json_text = jsonify(todos)
    return json_text #The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list (todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True) # { "done": true, "label": "Sample Todo 2" }
    todos.append(request_body)
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