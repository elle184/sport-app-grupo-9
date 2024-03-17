from flaskr import create_app
from .modelos import *
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from .vistas import VistaLogin,VistaPermisos,VistaEventos

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

CORS(
        app,
        origins="*",
    )

api = Api(app)
api.add_resource(VistaLogin,'/login')
api.add_resource(VistaPermisos,'/permisos','/permisos/<int:id_usuario>')
api.add_resource(VistaEventos,'/evento')

jwt = JWTManager(app)


