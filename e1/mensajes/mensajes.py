from celery import Celery

celery_app = Celery(__name__, brokwe='redis://localhost:6000/0')

@celery_app.task()
def registrar_usuarioevento(usuario, evento, fecha):
    with open('log_registro.txt', 'a+') as file:
        file.write('{} - registro usuarios a eventos: {}{}\n'.format(usuario, evento, fecha))