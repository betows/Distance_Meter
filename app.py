from flask_bootstrap import Bootstrap
from flask import Flask
from extensions import database, commands
from config import DevelopmentConfig

# blueprint import
from blueprints.main.views import main
from blueprints.locator.views import locator


def create_app():
    app = Flask(__name__)

    # setup with the configuration provided by the user / environment
    app.config.from_object(DevelopmentConfig)
    
    # setup all our dependencies
    database.init_app(app)
    commands.init_app(app)
    
    # register blueprint    
    app.register_blueprint(main)
    app.register_blueprint(locator)

    # set up bootstrap
    Bootstrap(app)
    
    return app


if __name__ == "__main__":
    create_app().run()
