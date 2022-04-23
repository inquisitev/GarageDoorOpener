from tinydb import TinyDB, Query

"""
Manage a session for a user by adding them to a database. 

Later, retrieve permission level or email for a user. 
"""

PRIVILAGES = ['OWNER', 'VISITOR']

class SessionManager:

    def __init__(self, db_path):
        self.db = TinyDB(db_path)

    def user_authenticated(self, token, privilage, email):
        if privilage in PRIVILAGES:
            self.db.insert({'token': token, 'privilage': privilage, 'email': email})

    def _check_privilage_level(self, token, privilage):
        authed_token = Query()
        result = self.db.search(authed_token.token == token)
        
        if not result:
            return False
        else: 
            return result[0]['privilage'] == privilage

    def owner_privilage(self, token):
        return self._check_privilage_level(token, 'OWNER')

    def visitor_privilage(self, token):
        return self._check_privilage_level(token, 'VISITOR')

    def get_email(self, token):
        authed_token = Query()
        result = self.db.search(authed_token.token == token)

        if not result:
            return None
        else: 
            return result[0]['email']
