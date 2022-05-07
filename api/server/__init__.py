from server.app.app import make_app
import os

DB_PATH = './data/db.json'

if os.path.exists(DB_PATH):
  if os.name == 'posix':
    from server.GarageDoorAdapters.pi.PiFaceDoorAdapter import PiFaceDoorAdapter
    api,cors = make_app(DB_PATH, PiFaceDoorAdapter())
  else:
    from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
    api,cors = make_app(DB_PATH, GenericGarageDoorAdapter())
    