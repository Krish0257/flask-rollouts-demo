from prometheus_client import Counter
from prometheus_flask_exporter import PrometheusMetrics

# Business Metrics
REQUEST_COUNTER = Counter(
    "inventory_requests_total",
    "Total inventory API requests"
)

FAILED_REQUEST_COUNTER = Counter(
    "inventory_failed_requests_total",
    "Total failed inventory API requests"
)

PRODUCT_CREATED_COUNTER = Counter(
    "inventory_products_created_total",
    "Total products created"
)

PRODUCT_UPDATED_COUNTER = Counter(
    "inventory_products_updated_total",
    "Total products updated"
)

PRODUCT_DELETED_COUNTER = Counter(
    "inventory_products_deleted_total",
    "Total products deleted"
)


def init_metrics(app):
    """
    Initialize Prometheus metrics.
    Metrics are automatically exposed at /metrics.
    """

    metrics = PrometheusMetrics(app)

    metrics.info(
        "inventory_service",
        "Inventory Service Information",
        version=app.config["APP_VERSION"],
        environment=app.config["ENVIRONMENT"],
    )

    return metrics