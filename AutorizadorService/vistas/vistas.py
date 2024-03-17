from flask_restful import Resource

class VistaAutorizacion(Resource) : 
    
    def get(self) :
        return "Hola, Mundo!"