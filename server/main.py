from app import make_app

make_app('./data/db.json').run('192.168.0.152', 8080)