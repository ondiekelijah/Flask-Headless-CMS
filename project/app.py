# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_simplemde import SimpleMDE
from flaskext.markdown import Markdown


# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
simplemde = SimpleMDE()



def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.secret_key = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SIMPLEMDE_JS_IIFE"] = True 
    app.config["SIMPLEMDE_USE_CDN"] = True


    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)
    simplemde.init_app(app)
    mkdwn = Markdown(app, extensions=["nl2br", "fenced_code"])


    # Register blueprints
    from auth.routes import auth
    from api.routes import api
    from studio.routes import studio

    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.register_blueprint(studio)


    return app
