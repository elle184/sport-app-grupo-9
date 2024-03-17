from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..modelos import Usuario, Evento,db
import datetime



class VistaEventos(Resource):

    @jwt_required()
    def post(self):
        print("entro al meotodo")
        
        id_funcionalidad = request.json["id_funcionalidad"]

        if id_funcionalidad == 1:
            evento = Evento(nombre=request.json["nombre"], deporte=request.json["deporte"], lugar=request.json["lugar"],fecha=request.json["fecha"], creado_por=request.json["id_usuario"])
            db.session.add(evento)
            db.session.commit()
            return{"respuesta":"El evento se creo de manera exitosa" }
        else:
            return{"respuesta":"el usuario no tiene permiso para crear un evento" }


