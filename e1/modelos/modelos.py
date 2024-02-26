from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    user = db.Column(db.String(500))
    password = db.Column(db.String(128))
    eventos = db.relationship('Evento', secondary='evento_usuario', back_populates="usuarios")

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    usuarios = db.relationship('Usuario', secondary = 'evento_usuario', back_populates="eventos")

# class EventoUsuario(db.Model) :
#    usuario_id = db.Column(db.Integer)
#    evento_id = db.Column(db.Integer)

eventos_usuarios = db.Table('evento_usuario', 
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('evento_id', db.Integer, db.ForeignKey('evento.id'), primary_key=True))

class EventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Evento
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

# class EventoUsuarioSchema(SQLAlchemyAutoSchema) :
#    class Meta :
#        model = EventoUsuario
#        include_relationships = False
#        load_instance = True