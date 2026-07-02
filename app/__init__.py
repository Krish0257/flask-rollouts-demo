from flask import Flask
from app.routes import register_routes
from app.metrics import init_metrics
from app.config import Config
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_metrics(app)
    register_routes(app)

    logger.info(
        "Starting %s version %s",
        app.config["APP_NAME"],
        app.config["APP_VERSION"],
    )

    return app