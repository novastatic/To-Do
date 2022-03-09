# Programname: To-Do Liste - Pythonserver mit Flask
# Authors: Antonia Lenz, C. Wichmann (took codesnippets from beispiel-server.py)
# Date of initial creation: 2. Februar 2022

# import lib for creating unique IDs
import uuid 

# import flask and other libs
from flask import Flask, request, jsonify, abort

# initialisiere Flask-Server
app = Flask(__name__)

# create unique id for lists, users, entries
user_id_bob = uuid.uuid4()
user_id_alice = uuid.uuid4()
user_id_eve = uuid.uuid4()
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = uuid.uuid4()
todo_2_id = uuid.uuid4()
todo_3_id = uuid.uuid4()
todo_4_id = uuid.uuid4()

# define internal data structures with example data
user_list = [
    {'id': user_id_bob, 'name': 'Bob'},
    {'id': user_id_alice, 'name': 'Alice'},
    {'id': user_id_eve, 'name': 'Eve'},
]
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeit'},
    {'id': todo_list_3_id, 'name': 'Privat'},
]
todos = [
    {'id': todo_1_id, 'name': 'Milch', 'description': '', 'list': todo_list_1_id, 'user': user_id_bob},
    {'id': todo_2_id, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': todo_list_2_id, 'user': user_id_alice},
    {'id': todo_3_id, 'name': 'Kinokarten kaufen', 'description': '', 'list': todo_list_3_id, 'user': user_id_eve},
    {'id': todo_3_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id, 'user': user_id_eve},
]

# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# define route for mainpage with some minimal HTML-frontend
@app.route('/')
def index():
    return '<h1>Welcome to your Todo-List Hub</h1>'   

# show one list according to its id if it exists
@app.route('/todo-list/<list_id>', methods=["GET"])
def getListItem(list_id):
    # check if list exists
    for todo_list in todo_lists:
        if todo_list['id'] == list_id:
            list_item = todo_list
    if not list_item:
        abort(404)
    # return 200-JSON if list exists
    print('Getting requested list...')
    return jsonify([i for i in todos if i['list'] == list_id]), 200

# define route for deleting a specified list
@app.route('/todo-list/<list_id>', methods=["DELETE"])
def deleteList(list_id):
    # check if list exists
    for todo_list in todo_lists:
        if todo_list['id'] == list_id:
            list_item = todo_list
    if not list_item:
        abort(404)
    # remove list if it exists
    print('The list is being deleted...')
    todo_lists.remove(list_item)
    return '', 200

# define route for creating a new list
@app.route('/todo-list/', methods=["POST"])
def addList():
    # add new list + generate uuid
    new_list = request.get_json(force=True)
    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)
    print('The list is being created...')
    # return on creation
    return jsonify(new_list), 200

# define route to create a new entry in a specified list
@app.route('/todo-list/<list_id>/entry', methods=["POST"])
def addEntry():
    # add new entry + generate uuid
    new_entry = request.get_json(force=True)
    new_entry['id'] = uuid.uuid4()
    todos.append(new_entry)
    print('New entry is being created...')
    # return on creation
    return jsonify(new_entry), 200

# define route to update an existing entry on a specified list
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=["PUT"])
def updateEntry(entry_id):
    # update the specified entry according to the entry_id
    todos.append(entry_id)
    print('The selected entry is being updated...')
    return jsonify(entry_id), 200
    
# define route to delete an existing entry on a specified list
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=["DELETE"])
def deleteEntry(entry_id):
    # check if entry exists
    for todo in todos:
        if todo['id'] == entry_id:
            list_item = todo
    if not list_item:
        abort(404)
    # remove selected entry
    todos.remove(entry_id)
    print('The selected entry is being deleted...')
    return '', 200

# define route to show all users
@app.route('/user', methods=["GET"])
def getUsers():
    # get all existing users
    print('Getting all users...')
    return jsonify(user_list)

# define route to create a new user
@app.route('/user', methods=["POST"])
def createUser():
    # add new user + name and generate uuid
    new_user = request.get_json(force=True)
    new_user['id'] = uuid.uuid4()
    new_user['name'] = 'Pythonia'
    todo_lists.append(new_user)
    print('A new user is being created...')
    return jsonify(new_user), 200

# definiere Route für das Löschen eines Benutzers
@app.route('/user/<user_id>', methods=["DELETE"])
def deleteUser(user_id):
    # check if user exists and delete or return 404
    for user in user_list:
        if user['id'] == user_id:
            user_item = user
    if not user_item:
        abort(404)
    print('The user is being removed...')
    user_list.remove(user_item)
    return '', 200

# start application with flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)