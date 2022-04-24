from server.app.app import make_app
from server.GarageDoorAdapters.pi import PiFaceDoorAdapter

make_app('./data/db.json', PiFaceDoorAdapter).run('localhost', 8080)