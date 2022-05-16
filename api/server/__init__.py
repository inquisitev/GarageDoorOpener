from shelve import DbfilenameShelf
from server.app.app import make_app
import os

DB_FOLDER = './data'
DB_PATH = f"{DB_FOLDER}/db.json"

if not os.path.exists(DB_FOLDER):
  os.mkdir(DB_FOLDER)

if os.name == 'posix':
  from server.GarageDoorAdapters.pi.PiFaceDoorAdapter import PiFaceDoorAdapter
  api,cors = make_app(DB_PATH, PiFaceDoorAdapter())
else:
  from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
  api,cors = make_app(DB_PATH, GenericGarageDoorAdapter())
    