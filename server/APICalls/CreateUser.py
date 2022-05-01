import requests,json

URL = "http://127.0.0.1:8080/signup"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'user':'testUser3', 'email':"test2@test2.com", 'password_plain':"testpw"}
  
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# sending get request and saving the response as response object
r = requests.post(url = URL, data = json.dumps(PARAMS), headers=headers)