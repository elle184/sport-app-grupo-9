from flask import request
from flask_restful import Resource
from ..modelos import Usuario, db, Rol ,Permisos, Funcionalidad, FuncionalidadesSchema

class VistaPermisos(Resource):

    

    def get(self, id_usuario):
        print('usuario entrando: ' + str(id_usuario))
        funcionalidadesList = []        
        usuario = Usuario.query.filter(Usuario.id == id_usuario).first()    
        #rol = Rol.query.filter(Rol.id == usuario.id_rol).first
        permisos = Permisos.query.filter(Permisos.id_rol==usuario.id_rol)
        
        for permiso in permisos:
            print('el id funcionalidad es: ' + str(permiso.id_funcionalidad))
            funcionalidad = Funcionalidad.query.filter(Funcionalidad.id == permiso.id_funcionalidad)
            #print('el nombre de la funcionalidad es: ' + funcionalidad.nombre)
            funcionalidadesList.append(funcionalidad)

        return [FuncionalidadesSchema.dump(fun) for fun in funcionalidadesList]



