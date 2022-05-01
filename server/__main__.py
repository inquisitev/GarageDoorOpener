from server.app.app import make_app
import os

if os.name == 'posix':
  from server.GarageDoorAdapters.pi.PiFaceDoorAdapter import PiFaceDoorAdapter
  app,cors = make_app('./data/db.json', PiFaceDoorAdapter())
else:
  from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
  app,cors = make_app('./data/db.json', GenericGarageDoorAdapter())
  
app.run('127.0.0.1', 8080)