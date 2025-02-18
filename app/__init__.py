from flask import Flask

from app.database import init_chroma
from app.services.vector import VectorService
from config import ProductionConfig
import logging
from logging.handlers import RotatingFileHandler
import os


def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    chroma_collection = init_chroma()

    vector = VectorService(chroma_collection)

    # Make vector_store available to all routes
    app.vector = vector

    # Logging setup (as before)
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Flask app startup')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app