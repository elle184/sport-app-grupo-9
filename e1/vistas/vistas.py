from flask_restful import Resource
from modelos import db, Evento, Usuario, EventoSchema, UsuarioSchema
from flask import request
from datetime import datetime
from mensajes import registrar_usuarioevento
from marshmallow import ValidationError


usuario_schema = UsuarioSchema()
# evento_usuario_schema = EventoUsuarioSchema()

class VistaUsuarioEvento(Resource):

    def get(self, id_usuario):
        usuarios = Usuario.query.filter(Usuario.id == id_usuario)
        print(usuarios)
        return usuario_schema.dump(usuarios, many=True)

    def post(self):
        dato = request.json
        print(dato)

        usuario_id = int(dato['id_usuario'])
        evento_id = int(dato['id_evento'])

        nuevo_usuario = Usuario.query.filter(Usuario.id == usuario_id).one()
        evento = Evento.query.filter(Evento.id == evento_id).one()

        print(nuevo_usuario)
        print(evento)

        if nuevo_usuario is None or evento is None:
            return 'Usuario o evento no existe', 404
        else:
            evento.usuarios.append(nuevo_usuario)
            nuevo_usuario.eventos.append(evento)
            db.session.commit()
            nombre = nuevo_usuario.nombre
            # registrar_usuarioevento.delay(nombre, evento_id, datetime.utcnow())
            return 'Registro exitoso', 200
        
    