from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experimento1.db'
    app.config['SLQALCHEMY_TRACK_NOTIFICACIONS'] = False
    return app