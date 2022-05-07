import json
from flask import request
from server.Exceptions.AuthenticationException import AuthenticationException

def make_end_points(app, session_manager, door_opener):
    @app.route('/door_button', methods=['POST'])
    def door_button():
        data = json.loads(request.data)
        token = data['token']
        if session_manager.visitor_privilage(token):
            door_opener.garage_door_button()
            return json.dumps({'state': door_opener.garage_door_state()}), 200
        else:
            return json.dumps({'error': "Invalid Permissions"}),401

    @app.route('/door_state', methods=['POST'])
    def door_state(): 
        data = json.loads(request.data)
        token = data['token']
        if session_manager.visitor_privilage(token):
            door_opener.garage_door_button()
            return json.dumps({'state': door_opener.garage_door_state()}), 200
        else:
            return json.dumps({'error': "Invalid Permissions"}),401
