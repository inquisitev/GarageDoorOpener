from server.app.app import make_app
import json, os

def test_new_user_endpoint_good():

  # good response with a valid new user
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  app = make_app('./tempdb.json').test_client()
  res = app.post('/signup', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js

def test_new_euser_aleady_exists():

  #bad response when a user already exists
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  app = make_app('./tempdb.json').test_client()
  res = app.post('/signup', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js

  res = app.post('/signup', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 409
  assert 'token' not in js
  assert 'error' in js
  assert js['error'] == "Account already exists"


def test_can_log_in():

  # good response logging in a user that exists with correct creds
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  app = make_app('./tempdb.json').test_client()
  res = app.post('/signup', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js

  app = make_app('./tempdb.json').test_client()
  res = app.post('/login', data=json.dumps({
    'user': 'test',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js

def test_good_creds_only():

  # good response logging in a user that exists with correct creds
  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  app = make_app('./tempdb.json').test_client()
  res = app.post('/signup', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js

  app = make_app('./tempdb.json').test_client()
  res = app.post('/login', data=json.dumps({
    'user': 'test',
    'password_plain': 'testpassword12345678butitswrong',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 401
  assert 'token' not in js
  assert 'error' in js
  assert js['error'] == "Wrong password"



  app = make_app('./tempdb.json').test_client()
  res = app.post('/login', data=json.dumps({
    'user': 'testwrongname',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 401
  assert 'token' not in js
  assert 'error' in js
  assert js['error'] == "No account with provided username"

  