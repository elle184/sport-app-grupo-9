from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from ..modelos import Usuario, db

class VistaLogin(Resource):


    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],Usuario.contrasena == request.json["contrasena"]).first()

        if usuario is None:
            return "Verifique los datos ingresados", 404
        token_de_acceso = create_access_token(identity=usuario.id)
        return {"mensaje": "Inicio de sesion exitoso", "token": token_de_acceso}
    
        
