import logging

from flask import Flask

from app.config import Config
from app.metrics import init_metrics
from app.routes import register_routes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


def create_app():
    """
    Create and configure the Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Prometheus metrics
    init_metrics(app)

    # Register application routes
    register_routes(app)

    logger.info(
        "Starting application=%s version=%s environment=%s",
        app.config["APP_NAME"],
        app.config["APP_VERSION"],
        app.config["ENVIRONMENT"],
    )

    return app