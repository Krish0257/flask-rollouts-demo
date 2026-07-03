import random
import time

from flask import current_app, jsonify, request

from app.config import Config
from app.metrics import (
    FAILED_REQUEST_COUNTER,
    PRODUCT_CREATED_COUNTER,
    PRODUCT_DELETED_COUNTER,
    PRODUCT_UPDATED_COUNTER,
    REQUEST_COUNTER,
)

# =====================================================================
# Demo In-Memory Database
# =====================================================================

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000,
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 2500,
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 1200,
    },
]


# =====================================================================
# Helper Functions
# =====================================================================

def should_fail():
    """
    Simulate failures for Argo Rollouts analysis.

    Returns:
        bool: True if the request should fail.
    """
    return random.random() < Config.FAILURE_RATE


def simulate_latency():
    """
    Simulate response latency for rollout testing.
    """
    if Config.RESPONSE_DELAY > 0:
        time.sleep(Config.RESPONSE_DELAY)


def record_request():
    """
    Record an incoming API request.
    """
    REQUEST_COUNTER.inc()


def record_failure():
    """
    Record a failed API request.
    """
    FAILED_REQUEST_COUNTER.inc()


def error_response(message, status_code):
    """
    Return a standardized JSON error response.
    """
    return jsonify({"message": message}), status_code


# =====================================================================
# Route Registration
# =====================================================================

def register_routes(app):

    @app.before_request
    def log_request():
        current_app.logger.info(
            "%s %s",
            request.method,
            request.path,
        )

    @app.route("/")
    def home():
        """
        Application information endpoint.
        """
        return jsonify(
            {
                "application": current_app.config["APP_NAME"],
                "version": current_app.config["APP_VERSION"],
                "environment": current_app.config["ENVIRONMENT"],
                "status": "Running",
            }
        )

    @app.route("/health")
    def health():
        """
        Kubernetes liveness probe.
        """
        return jsonify({"status": "UP"})

    @app.route("/ready")
    def ready():
        """
        Kubernetes readiness probe.
        """
        return jsonify({"status": "READY"})

    @app.route("/api/products", methods=["GET"])
    def get_products():
        """
        Return all products.
        """
        record_request()

        simulate_latency()

        if should_fail():
            record_failure()
            return error_response("Internal Server Error", 500)

        current_app.logger.info("Retrieved %d products", len(products))

        return jsonify(products)

    @app.route("/api/products/<int:product_id>", methods=["GET"])
    def get_product(product_id):
        """
        Return a product by ID.
        """
        record_request()

        simulate_latency()

        if should_fail():
            record_failure()
            return error_response("Internal Server Error", 500)

        product = next(
            (p for p in products if p["id"] == product_id),
            None,
        )

        if product is None:
            current_app.logger.warning(
                "Product with id=%s not found",
                product_id,
            )
            return error_response("Product not found", 404)

        current_app.logger.info(
            "Retrieved product id=%s",
            product_id,
        )

        return jsonify(product)

    @app.route("/api/products", methods=["POST"])
    def create_product():
        """
        Create a new product.
        """
        record_request()

        simulate_latency()

        if should_fail():
            record_failure()
            return error_response("Internal Server Error", 500)

        data = request.get_json()

        if not data:
            return error_response("Request body is required", 400)

        if "name" not in data or "price" not in data:
            return error_response("name and price are required", 400)

        product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"],
        }

        products.append(product)

        PRODUCT_CREATED_COUNTER.inc()

        current_app.logger.info(
            "Created product id=%s name=%s",
            product["id"],
            product["name"],
        )

        return jsonify(product), 201

    @app.route("/api/products/<int:product_id>", methods=["PUT"])
    def update_product(product_id):
        """
        Update an existing product.
        """
        record_request()

        simulate_latency()

        if should_fail():
            record_failure()
            return error_response("Internal Server Error", 500)

        data = request.get_json()

        if not data:
            return error_response("Request body is required", 400)

        if "name" not in data or "price" not in data:
            return error_response("name and price are required", 400)

        product = next(
            (p for p in products if p["id"] == product_id),
            None,
        )

        if product is None:
            current_app.logger.warning(
                "Product with id=%s not found",
                product_id,
            )
            return error_response("Product not found", 404)

        product["name"] = data["name"]
        product["price"] = data["price"]

        PRODUCT_UPDATED_COUNTER.inc()

        current_app.logger.info(
            "Updated product id=%s",
            product_id,
        )

        return jsonify(product)

    @app.route("/api/products/<int:product_id>", methods=["DELETE"])
    def delete_product(product_id):
        """
        Delete a product.
        """
        record_request()

        simulate_latency()

        if should_fail():
            record_failure()
            return error_response("Internal Server Error", 500)

        product = next(
            (p for p in products if p["id"] == product_id),
            None,
        )

        if product is None:
            current_app.logger.warning(
                "Product with id=%s not found",
                product_id,
            )
            return error_response("Product not found", 404)

        products.remove(product)

        PRODUCT_DELETED_COUNTER.inc()

        current_app.logger.info(
            "Deleted product id=%s",
            product_id,
        )

        return "", 204