from collections import UserList
from hashlib import new
from tinydb import TinyDB, Query
from uuid import uuid4
from cryptography.fernet import Fernet
from server.Exceptions.AuthenticationException import AuthenticationException
import os

if os.path.exists('./enc.txt'):
    with open('./enc.txt', 'rb') as enc:
        key = enc.read()
else:
    with open('./enc.txt', 'wb') as enc:
        key = Fernet.generate_key()
        enc.write(key)


    
"""
Manage a session for a user by adding them to a database. 

Later, retrieve permission level or email for a user. 
"""

OWNER = 4
RESIDENT = 3
VISITOR = 2
UNVERIFIED = 1

WRONG_PASSWORD_MESSAGE = "Wrong password"
WRONG_USER_NAME_MESSAGE = "No account with provided username"

class SessionManager:

    def __init__(self, db_path):
        self.db = TinyDB(db_path)

    def encrypted_password(self, password):
        return Fernet(key).encrypt(password.encode())

    def decrypted_password(self, encrypted_password):
        enc = Fernet(key).decrypt(encrypted_password)
        return enc

    def make_token(self):
        token = uuid4().hex
        return token


    def new_user(self, user_name, email, password_plain):
        user_list = Query()

        result = self.db.search(user_list.privilage == OWNER)
        num_users = len(result)

        if num_users == 0:
            priv = OWNER
        else:
            priv = UNVERIFIED

        user_list = Query()
        result = self.db.search((user_list.user_name == user_name) | (user_list.email == email))
        num_users = len(result)

        if num_users > 0:
            raise AuthenticationException("Account already exists")

        new_entry = {
            'token': self.make_token(), 
            'user_name': user_name,
            'password_hash': self.encrypted_password(password_plain).decode(),
            'privilage': priv,
            'email': email
            }

        self.db.insert(new_entry)
        return new_entry['token']
        
    def get_token(self, user_name, password_plain):
        authed_token = Query()
        result = self.db.search(authed_token.user_name == user_name)

        if not result:
            raise AuthenticationException(WRONG_USER_NAME_MESSAGE)
        else: 
            hashed_password = result[0]['password_hash'].encode()
            decrypted_password = self.decrypted_password(hashed_password).decode()

            if decrypted_password == password_plain:
                return result[0]['token']
            else:
                raise AuthenticationException(WRONG_PASSWORD_MESSAGE)

    def _check_privilage_level(self, token, privilage):
        authed_token = Query()
        result = self.db.search(authed_token.token == token)
        
        if not result:
            return False
        else: 
            users_priviage = result[0]['privilage']
            return users_priviage >= privilage

    def owner_privilage(self, token):
        return self._check_privilage_level(token, OWNER)

    def resident_privilage(self, token):
        return self._check_privilage_level(token, RESIDENT)

    def visitor_privilage(self, token):
        return self._check_privilage_level(token, VISITOR)

    def unverified_privilage(self, token):
        return self._check_privilage_level(token, UNVERIFIED)

    def get_email(self, token):
        authed_token = Query()
        result = self.db.search(authed_token.token == token)

        if not result:
            return None
        else: 
            return result[0]['email']
