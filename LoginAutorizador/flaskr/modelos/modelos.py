from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Usuario(db.Model):
    __table_args__ = (UniqueConstraint('usuario', name='unique_username'),)
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    id_rol=db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable = True)

class Rol(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre_rol=db.Column(db.String(50),nullable=False)
    descripcion=db.Column(db.String(100),nullable=False)

class Funcionalidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    descripcion=db.Column(db.String(300),nullable=False)

class Permisos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'))
    id_funcionalidad = db.Column(db.Integer, db.ForeignKey('funcionalidad.id'))

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    deporte = db.Column(db.String(128), nullable=False)
    lugar = db.Column(db.String(128), nullable=True)
    fecha = db.Column(db.String(30), nullable=True)
    creado_por = db.Column(db.Integer, db.ForeignKey('usuario.id'))


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
        exclude = ('contrasena',)

class EventoSchema(SQLAlchemyAutoSchema):
    creado_por = fields.Integer()
    class Meta:
        model = Evento
        include_relationships = True
        load_instance = True

class FuncionalidadesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Funcionalidad
        include_relationships = True
        load_instance = True



#class RolSchema(SQLAlchemyAutoSchema):
#    class Meta:
#        model = Rol
#        include_relationships = True
#        load_instance = True