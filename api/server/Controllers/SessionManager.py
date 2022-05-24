import json
from tinydb import TinyDB, Query
from uuid import uuid4
from server.Exceptions.AuthenticationException import AuthenticationException
import os, hashlib, binascii

    
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
ACCOUNT_EXISTS_MESSAGE = "Account already exists"

EMAIL_KEY = 'email'
TOKEN_KEY = 'token'
USER_NAME_KEY = 'user_name'
PRIVILAGE_KEY = 'privilage'
PASSWORD_HASH_KEY = 'password_hash'
PASSWORD_HASH_SALT_KEY = 'password_salt'

class SessionManager:

    def __init__(self, db_path):
        self.db = TinyDB(db_path, create_dirs=True)

    def _encrypted_password(self, password, salt = None):
        if salt is None:
            salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt, key

    def _authenticate(self, salt, key, attempt):

        hashed_attempt = self._encrypted_password(attempt, salt)
        return hashed_attempt[1] == key

    def _make_token(self):
        token = uuid4().hex
        return token


    def new_user(self, user_name, email, password_plain):
        """
        Add a new user. 

        If its the first user, make them the owner.
        otherwise they are unverified until promoted. 

        Also check that a user exists with the email.

        If all goes well, return the new token. 
        """
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
            raise AuthenticationException(ACCOUNT_EXISTS_MESSAGE)

        salt,key = self._encrypted_password(password_plain)

        new_entry = {
            TOKEN_KEY: self._make_token(), 
            USER_NAME_KEY: user_name,
            PASSWORD_HASH_SALT_KEY: binascii.hexlify(salt).decode(),
            PASSWORD_HASH_KEY: binascii.hexlify(key).decode(),
            PRIVILAGE_KEY: priv,
            EMAIL_KEY: email
            }

        self.db.insert(new_entry)
        return new_entry[TOKEN_KEY]
        
    def get_token(self, user_name, password_plain):
        """
        Log a user in. Authentication error on either wrong user name or wrong password.
        """
        authed_token = Query()
        result = self.db.search(authed_token.user_name == user_name)

        if result:
            hashed_password = binascii.unhexlify(result[0][PASSWORD_HASH_KEY])
            salt = binascii.unhexlify(result[0][PASSWORD_HASH_SALT_KEY])

            if self._authenticate(salt, hashed_password, password_plain):
                return result[0][TOKEN_KEY]
            else:
                raise AuthenticationException(WRONG_PASSWORD_MESSAGE)

        else: 
            raise AuthenticationException(WRONG_USER_NAME_MESSAGE)

    def _check_privilage_level(self, token, privilage):
        """
        Check a tokens privilage level, true if the owners privilage
        is atleast the checked privilage.
        """
        authed_token = Query()
        result = self.db.search(authed_token.token == token)
        
        if result:
            users_priviage = result[0][PRIVILAGE_KEY]
            return users_priviage >= privilage
        
        return False

    def owner_privilage(self, token):
        """
        Check that a token has been granted owner level privilage. 
        Owner includes privilages of resident, visitor and unverified. 
        """
        return self._check_privilage_level(token, OWNER)

    def resident_privilage(self, token):
        """
        Check that a token has been granted resident level privilage. 
        Resident includes privilages of visitor and unverified. 
        """
        return self._check_privilage_level(token, RESIDENT)

    def visitor_privilage(self, token):
        """
        Check that a token has been granted visitor level privilage. 
        Visitor includes privilages of unverified. 
        """
        return self._check_privilage_level(token, VISITOR)

    def unverified_privilage(self, token):
        """
        Basically no privilages until promoted.
        """
        return self._check_privilage_level(token, UNVERIFIED)

    def get_email(self, token):
        """
        Get a users email by the token.
        """
        authed_token = Query()
        result = self.db.search(authed_token.token == token)

        if not result:
            return None
        else: 
            return result[0][EMAIL_KEY]
