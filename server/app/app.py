#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from flask_cors import CORS
from server.EndPoints.SessionEndPoints import make_end_points as make_session_end_points
from server.EndPoints.GarageDoorEndpoints import make_end_points as make_door_end_points
from server.Controllers.SessionManager import SessionManager

def make_app(dbpath, opener = None):
    app = Flask(__name__)
    cors = CORS(app)

    app.config['CORS_HEADERS'] = 'application/json'
    @app.route('/')
    def index():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})
    session_manager = SessionManager(dbpath)
    make_session_end_points(app, session_manager)
    if opener is not None:
        make_door_end_points(app, session_manager, opener)
    
    return app, cors