# content of test_sample.py
from server.Controllers.SessionManager import SessionManager
from server.Exceptions.AuthenticationException import AuthenticationException
import pytest, os

good_user = [
    'temp user name', 
    'temp@temp.com',
    'password plain text',
]

unverified_user = [
    'temp user name 2', 
    'temp2@temp.com',
    'bad password text',
]

def test_new_user():
    if os.path.exists('./tempdb.json'):
        os.remove('./tempdb.json')
    sm = SessionManager('./tempdb.json')
    assert sm is not None

    # Can make a new first user.
    assert sm.new_user(*good_user)

    # Can make another user
    assert sm.new_user(*unverified_user)


def test_log_in():
    if os.path.exists('./tempdb.json'):
        os.remove('./tempdb.json')
    sm = SessionManager('./tempdb.json')
    assert sm is not None

    # Can make a new first user.
    assert sm.new_user(*good_user)

    # Can make another user
    assert sm.new_user(*unverified_user)

    # first user can log in
    assert sm.get_token(good_user[0], good_user[2])

    # second user can log in
    assert sm.get_token(unverified_user[0], unverified_user[2])

    # cannot log in with other users creds
    with pytest.raises(AuthenticationException):
        sm.get_token(good_user[0], unverified_user[2])

    # cannot log in with other users creds
    with pytest.raises(AuthenticationException):
        sm.get_token(unverified_user[0], good_user[2])

    # cannot log in with bad creds
    with pytest.raises(AuthenticationException):
        sm.get_token(unverified_user[0], "badpass")



def test_privilages():
    if os.path.exists('./tempdb.json'):
        os.remove('./tempdb.json')
    sm = SessionManager('./tempdb.json')
    assert sm is not None

    # Can make a new first user.
    token = sm.new_user(*good_user)

    # Can make another user
    assert sm.new_user(*unverified_user)

    # first user is owner. owner has all privilages
    assert sm.owner_privilage(sm.get_token(good_user[0], good_user[2]))
    assert sm.resident_privilage(sm.get_token(good_user[0], good_user[2]))
    assert sm.visitor_privilage(sm.get_token(good_user[0], good_user[2]))
    assert sm.unverified_privilage(sm.get_token(good_user[0], good_user[2]))


    assert sm.owner_privilage(token)
    assert sm.resident_privilage(token)
    assert sm.visitor_privilage(token)
    assert sm.unverified_privilage(token)

    # second user is unverified. they have minimal privilages
    assert not sm.owner_privilage(sm.get_token(unverified_user[0], unverified_user[2]))
    assert not sm.resident_privilage(sm.get_token(unverified_user[0], unverified_user[2]))
    assert not sm.visitor_privilage(sm.get_token(unverified_user[0], unverified_user[2]))
    assert sm.unverified_privilage(sm.get_token(unverified_user[0], unverified_user[2]))



