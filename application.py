from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return {"status": "200",
            "msg": "exitoso",
            "result":" Accion correcta"}