from flask import jsonify, request, current_app
from app.config import Config
from app.metrics import (
    REQUEST_COUNTER,
    FAILED_REQUEST_COUNTER,
    PRODUCT_CREATED_COUNTER,
    PRODUCT_UPDATED_COUNTER,
    PRODUCT_DELETED_COUNTER
)
import random
import time

# In-memory demo database
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 2500
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 1200
    }
]


def should_fail():
    """Return True based on configured failure rate."""
    return (
        random.random() < Config.FAILURE_RATE
        if Config.FAILURE_RATE > 0
        else False
    )


def simulate_latency():
    """Add artificial response delay if configured."""
    if Config.RESPONSE_DELAY > 0:
        time.sleep(Config.RESPONSE_DELAY)


def register_routes(app):

    @app.before_request
    def log_request():
        current_app.logger.info(
            "%s %s",
            request.method,
            request.path
        )

    @app.route("/")
    def home():
        return jsonify({
            "application": current_app.config["APP_NAME"],
            "version": current_app.config["APP_VERSION"],
            "environment": current_app.config["ENVIRONMENT"],
            "status": "Running"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "UP"
        })

    @app.route("/ready")
    def ready():
        return jsonify({
            "status": "READY"
        })

    @app.route("/api/products", methods=["GET"])
    def get_products():

        REQUEST_COUNTER.inc()

        simulate_latency()

        if should_fail():
            FAILED_REQUEST_COUNTER.inc()
            return jsonify({"message": "Internal Server Error"}), 500

        return jsonify(products)

    @app.route("/api/products/<int:product_id>", methods=["GET"])
    def get_product(product_id):

        REQUEST_COUNTER.inc()

        simulate_latency()

        if should_fail():
            FAILED_REQUEST_COUNTER.inc()
            return jsonify({"message": "Internal Server Error"}), 500

        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )

        if product is None:
            return jsonify({"message": "Product not found"}), 404

        return jsonify(product)

    @app.route("/api/products", methods=["POST"])
    def create_product():

        REQUEST_COUNTER.inc()

        simulate_latency()

        if should_fail():
            FAILED_REQUEST_COUNTER.inc()
            return jsonify({"message": "Internal Server Error"}), 500

        data = request.get_json()

        if not data or "name" not in data or "price" not in data:
            return jsonify({
                "message": "name and price are required"
            }), 400

        product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"]
        }

        products.append(product)

        PRODUCT_CREATED_COUNTER.inc()

        return jsonify(product), 201

    @app.route("/api/products/<int:product_id>", methods=["PUT"])
    def update_product(product_id):

        REQUEST_COUNTER.inc()

        simulate_latency()

        if should_fail():
            FAILED_REQUEST_COUNTER.inc()
            return jsonify({"message": "Internal Server Error"}), 500

        data = request.get_json()

        if not data or "name" not in data or "price" not in data:
            return jsonify({
                "message": "name and price are required"
            }), 400

        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )

        if product is None:
            return jsonify({"message": "Product not found"}), 404

        product["name"] = data["name"]
        product["price"] = data["price"]

        PRODUCT_UPDATED_COUNTER.inc()

        return jsonify(product)

    @app.route("/api/products/<int:product_id>", methods=["DELETE"])
    def delete_product(product_id):

        REQUEST_COUNTER.inc()

        simulate_latency()

        if should_fail():
            FAILED_REQUEST_COUNTER.inc()
            return jsonify({"message": "Internal Server Error"}), 500

        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )

        if product is None:
            return jsonify({"message": "Product not found"}), 404

        products.remove(product)

        PRODUCT_DELETED_COUNTER.inc()

        return "", 204