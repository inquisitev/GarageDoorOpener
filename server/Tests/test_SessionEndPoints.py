from server.app.app import make_app
import json 

def test_new_user_endpoint():
  app = make_app('./tempdb.json')
  response = app.post('/login', data={
    'user': 'test',
    'email': 'test@test.com',
    'password_plain': 'testpassword12345678',
    }, 
    content_type='application/json',)
  assert 'token' in json.loads(response.get_data())
  