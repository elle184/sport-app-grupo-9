from e1 import create_app
from flask_restful import Api 
from .modelos import db
from .vistas import VistaUsuarioEvento

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaUsuarioEvento, '/usuario/<int:id_usuario>')
api.add_resource(VistaUsuarioEvento, '/evento/<int>id_evento>')