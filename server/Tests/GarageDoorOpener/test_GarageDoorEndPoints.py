from server.app.app import make_app
from server.Tests.GarageDoorOpener.StubbedOpener import StubbedOpener
import json, os

def make_test_app():
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')

  opener = StubbedOpener([0, 1, 2],[3, 4, 5])
  app = make_app('./tempdb.json', opener).test_client()
  return app

def make_a_user(app, creds):
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  res = app.post('/signup', data=json.dumps(creds), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js
  return js['token']


def test_door_open_with_good_privilages():
  app = make_test_app()
  token = make_a_user(app, {
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }
  )

  res = app.post('/door_button', data=json.dumps({
    'token': token
    }), 
    content_type='application/json')

  assert res.status_code == 200



def test_get_door_state_with_good_privilages():
  app = make_test_app()
  token = make_a_user(app, {
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }
  )

  res = app.post('/door_state', data=json.dumps({
    'token': token
    }), 
    content_type='application/json')

  assert res.status_code == 200

def test_door_open_with_bad_privilages():
  app = make_test_app()
  owner = make_a_user(app, {
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }
  )


  unverified = make_a_user(app, {
    'user': 'test2',
    'email': 'test2@test.com',
    'password_plain': 'testpassword12345678',
    }
  )

  res = app.post('/door_button', data=json.dumps({
    'token': unverified
    }), 
    content_type='application/json')

  assert res.status_code == 401

def test_get_door_state_with_bad_privilages():
  app = make_test_app()
  owner = make_a_user(app, {
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }
  )


  unverified = make_a_user(app, {
    'user': 'test2',
    'email': 'test2@test.com',
    'password_plain': 'testpassword12345678',
    }
  )

  res = app.post('/door_state', data=json.dumps({
    'token': unverified
    }), 
    content_type='application/json')

  assert res.status_code == 401

  