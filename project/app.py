# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.secret_key = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)


    # Register blueprints
    from auth.routes import auth
    from api.routes import api
    from studio.routes import studio

    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.register_blueprint(studio)


    return app
