import json

def make_end_points(app, session_manager):
    @app.route('/login')
    def login():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})

    @app.route('/signup')
    def signup():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})

    @app.route('/forgotpass')
    def forgotpass():
        return json.dumps({'name': 'alice',
                        'email': 'alice@outlook.com'})