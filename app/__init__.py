from flask import Flask
from .config import Config
from .extensions import db, migrate, mallow
from .models import *


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    mallow.init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('X-Atonga-App', 'Atongas Rentals')
        return response

    from app.admin import admin_bp

    app.register_blueprint(admin_bp)

    return app
