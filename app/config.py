import os


class Config:
    """
    Application configuration loaded from environment variables.
    """

    APP_NAME = os.getenv("APP_NAME", "inventory-service")
    APP_VERSION = os.getenv("APP_VERSION", "v1.2.1")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "5000"))

    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    FAILURE_RATE = float(os.getenv("FAILURE_RATE", "0.5"))

    RESPONSE_DELAY = float(os.getenv("RESPONSE_DELAY", "0"))