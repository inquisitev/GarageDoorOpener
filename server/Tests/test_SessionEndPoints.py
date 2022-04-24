from server.app.app import make_app
import json, os

def test_new_user_endpoint_good():

  if os.path.exists('./tempdb.json'):
      os.remove('./tempdb.json')
  app = make_app('./tempdb.json').test_client()
  res = app.post('/login', data=json.dumps({
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }), 
    content_type='application/json')
  js = json.loads(res.data)
  assert res.status_code == 200
  assert 'token' in js
  