import json
from flask import request

def make_end_points(app, session_manager):
    @app.route('/login')
    def login():
        data = request.data
        token = session_manager.new_user(data['user'], data['email'], data['password_plain'])
        return json.dumps({'token': token})

    @app.route('/signup')
    def signup():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})

    @app.route('/forgotpass')
    def forgotpass():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})