#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from server.EndPoints.SessionEndPoints import make_end_points
from server.Controllers.SessionManager import SessionManager

def make_app(dbpath):
    app = Flask(__name__)
    @app.route('/')
    def index():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})
    session_manager = SessionManager(dbpath)
    make_end_points(app, session_manager)
    
    return app