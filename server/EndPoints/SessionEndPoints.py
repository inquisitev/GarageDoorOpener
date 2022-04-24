import json
from flask import request

def make_end_points(app, session_manager):
    @app.route('/login', methods=['POST'])
    def login(): 
        data = json.loads(request.data)
        token = session_manager.new_user(data['user'], data['email'], data['password_plain'])
        return json.dumps({'token': token}), 200

    @app.route('/signup')
    def signup():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})

    @app.route('/forgotpass')
    def forgotpass():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})