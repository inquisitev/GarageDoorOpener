#!/usr/bin/env python
# encoding: utf-8
import json
from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask_cors import CORS
from server.EndPoints.SessionEndPoints import make_end_points as make_session_end_points
from server.EndPoints.GarageDoorEndpoints import make_end_points as make_door_end_points
from server.Controllers.SessionManager import SessionManager

def make_app(dbpath, opener = None):

    app = APIFlask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'application/json'
    @app.get('/')
    @app.doc(summary='Say hello', description='Some description for the /hello')
    def index():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})
    session_manager = SessionManager(dbpath)
    make_session_end_points(app, session_manager)
    if opener is not None:
        make_door_end_points(app, session_manager, opener)
    
    return app, cors