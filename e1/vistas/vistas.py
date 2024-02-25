from flask_restful import Resource
from ..modelos import db, Evento, Usuario, EventoSchema, UsuarioSchema
from flask import request
from datetime import datetime
from ..mensajes import registrar_usuarioevento

usuario_schema = UsuarioSchema()

class VistaUsuarioEvento(Resource):

    def get(self, id_usuario):
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))

    def post(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)

        if "id_usuario" in request.json.keys():
            nuevo_usuario = Usuario.query.get(request.json["id_usuario"])
            if nuevo_usuario is not None:
                nuevo_usuario.eventos.append(evento)
                evento.usuarios.append(nuevo_usuario)
                db.session.commit()
                nombre = request.json("nombre")
                idevento = request.json("id_evento")
                registrar_usuarioevento.delay(nombre, idevento, datetime.utcnow())
                return 'Registro exitoso', 204
            else:
                return 'Usuario equivocado', 404
        else:
            nuevo_usuario = Usuario(nombre=request.json['nombre'],\
                                user=request.json['user'],\
                                password=request.json['password'],\
                                eventos=request.json['evento'])
            nombre = request.json("nombre")
            idevento = request.json("id_evento")
            evento.usuarios.append(nuevo_usuario)
            db.session.commit()    
            registrar_usuarioevento.delay(nombre, idevento, datetime.utcnow())
            return 'Registro exitoso', 204    
        