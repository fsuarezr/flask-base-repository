from flask import Flask

# Routes
from .routes import IndexRoutes
# from .routes import AuthRoutes, IndexRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    # app.register_blueprint(AuthRoutes.main, url_prefix='/auth')

    return app