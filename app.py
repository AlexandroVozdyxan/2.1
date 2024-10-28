from flask import Flask
from flask import request
from werkzeug.serving import is_running_from_reloader

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/profile', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def profile(me): # /user or /me
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PUT':
        return 'PUT'
    if request.method == 'PATCH':
        return 'PATCH'
    if request.method == 'DELETE':
        return 'DELETE'
@app.route('/favourites', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def favourites():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'
    if request.method == 'PATCH':
        return 'PATCH'
@app.route('/favourites/<favourite_id>', methods=['DELETE'])
def favourite(favourite_id):
    if request.method == 'DELETE':
        return f'DELETE{favourite_id}'

@app.route('/search_history', methods=['GET', 'DELETE'])
def search_history():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def item(item_id):
    if request.method == 'GET':
        return f'GET {item_id}'
    if request.method == 'DELETE':
        return f'DELETE {item_id}'

@app.route('/leasers', methods=['GET'])
def leasers():
    if request.method == 'GET':
        return 'GET'

@app.route('/leasers/<leaser_id> ', methods=['GET'])
def leaser(leaser_id):
    if request.method == 'GET':
        return f'GET {leaser_id}'

@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/contracts/<contract_id>', methods=['GET', 'PATCH', 'PUT'])
def contract(contract_id):
    if request.method == 'GET':
        return f'GET {contract_id}'
    if request.method == 'POST':
        return f'POST {contract_id}'
    if request.method == 'PATCH':
        return f'PATCH {contract_id}'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/complain', methods=['POST'])
def complain():
    if request.method == 'POST':
        return 'POST'

@app.route('/compare', methods=['GET', 'PUT', 'PATCH'])
def compare():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PUT':
        return 'PUT'
    if request.method == 'PATCH':
        return 'PATCH'

if __name__ == '__main__':
    app.run()
