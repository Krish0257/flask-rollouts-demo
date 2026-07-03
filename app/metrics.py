"""
Prometheus metrics for the Inventory Service.

This module defines both application-level and business-level metrics.
Metrics are automatically exposed at the /metrics endpoint through
prometheus_flask_exporter.
"""

from prometheus_client import Counter
from prometheus_flask_exporter import PrometheusMetrics

# =====================================================================
# Business Metrics
# =====================================================================

REQUEST_COUNTER = Counter(
    "inventory_requests_total",
    "Total number of Inventory API requests"
)

FAILED_REQUEST_COUNTER = Counter(
    "inventory_failed_requests_total",
    "Total number of failed Inventory API requests"
)

PRODUCT_CREATED_COUNTER = Counter(
    "inventory_products_created_total",
    "Total number of products created"
)

PRODUCT_UPDATED_COUNTER = Counter(
    "inventory_products_updated_total",
    "Total number of products updated"
)

PRODUCT_DELETED_COUNTER = Counter(
    "inventory_products_deleted_total",
    "Total number of products deleted"
)


def init_metrics(app):
    """
    Initialize Prometheus metrics.

    Exposes:
        /metrics

    Registers:
        - Default Flask metrics
        - Custom business metrics
        - Application information metric
    """

    metrics = PrometheusMetrics(app)

    metrics.info(
        "inventory_service",
        "Inventory Service Information",
        version=app.config["APP_VERSION"],
        environment=app.config["ENVIRONMENT"],
    )

    return metrics