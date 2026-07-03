import os


class Config:
    """
    Centralized application configuration.

    All configuration values are loaded from environment variables
    with sensible defaults for local development.
    """

    # ------------------------------------------------------------------
    # Application Information
    # ------------------------------------------------------------------
    APP_NAME: str = os.getenv("APP_NAME", "inventory-service")
    APP_VERSION: str = os.getenv("APP_VERSION", "v1.2.1")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # ------------------------------------------------------------------
    # Server Configuration
    # ------------------------------------------------------------------
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "5000"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # ------------------------------------------------------------------
    # Demo Configuration
    #
    # These settings intentionally simulate failures and latency to
    # demonstrate Argo Rollouts automated canary analysis.
    # ------------------------------------------------------------------
    FAILURE_RATE: float = max(
        0.0,
        min(1.0, float(os.getenv("FAILURE_RATE", "0.5")))
    )

    RESPONSE_DELAY: float = max(
        0.0,
        float(os.getenv("RESPONSE_DELAY", "0"))
    )