from AutorizadorService import create_app
from .vistas import VistaAutorizacion
from flask_restful import Api

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaAutorizacion, '/welcome')