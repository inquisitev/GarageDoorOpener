import json
from flask import request
from server.Exceptions.AuthenticationException import AuthenticationException

def make_end_points(app, session_manager):
    
    @app.route('/signup', methods=['POST'])
    def signup():
        data = json.loads(request.data)
        try:
            token = session_manager.new_user(data['user'], data['email'], data['password_plain'])
            return json.dumps({'token': token}), 200
        except AuthenticationException as e:
            return json.dumps({'error': e.args[0]}),409

    @app.route('/login', methods=['POST'])
    def login(): 
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})

    @app.route('/forgotpass')
    def forgotpass():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})