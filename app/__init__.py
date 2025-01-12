from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    return app
