from server.app.app import make_app
import os

if os.name == 'posix':
  from server.GarageDoorAdapters.pi.PiFaceDoorAdapter import PiFaceDoorAdapter
  api,cors = make_app('./data/db.json', PiFaceDoorAdapter())
else:
  from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
  api,cors = make_app('./data/db.json', GenericGarageDoorAdapter())
  