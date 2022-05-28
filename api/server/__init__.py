from shelve import DbfilenameShelf
from server.app.app import make_app
import os

DB_FOLDER = './db_data'
DB_PATH = f"{DB_FOLDER}/db.json"

if not os.path.exists(DB_FOLDER):
  os.mkdir(DB_FOLDER)
  if os.name == 'posix':
    os.chmod(DB_FOLDER,0o777)

if os.environ.get("DOOR_ADAPTER") == 'piface':
    from server.GarageDoorAdapters.pi.PiFaceDoorAdapter import PiFaceDoorAdapter
    api,cors = make_app(DB_PATH, PiFaceDoorAdapter())
else:
  from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
  api,cors = make_app(DB_PATH, GenericGarageDoorAdapter())

 