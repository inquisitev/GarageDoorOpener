from server.app.app import make_app
from server.GarageDoorAdapters.pi import PiFaceDoorAdapter


app,cors = make_app('./data/db.json', PiFaceDoorAdapter)
app.run('127.0.0.1', 8080)