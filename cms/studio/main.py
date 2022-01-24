# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_simplemde import SimpleMDE
from flaskext.markdown import Markdown
from flask_moment import Moment
# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
simplemde = SimpleMDE()
moment = Moment()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    print(f'ENV is set to: {app.config["ENV"]}')

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)
    simplemde.init_app(app)
    mkdwn = Markdown(app, extensions=["nl2br", "fenced_code"])
    moment.init_app(app)

    # Register blueprints
    from cms.api.routes import api
    from cms.studio.routes import studio

    app.register_blueprint(api)
    app.register_blueprint(studio)

    return app
