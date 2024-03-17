from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from ..modelos import Usuario, Rol ,Permisos, Funcionalidad

class VistaPermisos(Resource):

    @jwt_required()
    def get(self, id_usuario):

        funcionalidadesList = []        
        usuario = Usuario.query.filter(Usuario.id == id_usuario).first()
        permisos = Permisos.query.filter(Permisos.id_rol==usuario.id_rol).all()
        for permiso in permisos:
            funcionalidad = Funcionalidad.query.filter(Funcionalidad.id == permiso.id_funcionalidad).first()

            funcionalidadesList.append({
                "Id": funcionalidad.id,
                "nombre": funcionalidad.nombre,
                "descripcion": funcionalidad.descripcion})
            
        return {"Funcionalidades": funcionalidadesList}

