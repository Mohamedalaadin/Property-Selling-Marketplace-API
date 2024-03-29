from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import Config


db = SQLAlchemy()
cache = Cache()     # Initialize cache

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cache.init_app(app)

    # Importing models
    from app import models

    # Import blueprints
    from .views import property_blueprint, search_blueprint, propertyDetails_blueprint

    # Register blueprints
    app.register_blueprint(property_blueprint, url_prefix='/api')
    app.register_blueprint(search_blueprint, url_prefix='/api')
    app.register_blueprint(propertyDetails_blueprint, url_prefix='/api')

    return app
