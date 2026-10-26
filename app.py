import os

from flask import Flask, jsonify, request

app = Flask(__name__)

DISCOUNT_CODES = {"VDAY20": 0.20}


def calculate_total(subtotal, code=None):
    """Return the cart total after applying a discount code."""
    if subtotal < 0:
        raise ValueError("Subtotal can't be negative")
    discount = DISCOUNT_CODES.get(code, 0)
    return round(subtotal * (1 - discount), 2)


def valentines_sale_on():
    """A simple feature flag: read from a setting, off by default."""
    return os.getenv("VALENTINES_SALE", "off") == "on"


ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    if valentines_sale_on():
        message = "Valentine's sale! Use code VDAY20 for 20% off."
    else:
        message = "Welcome to the flower shop."
    return jsonify(environment=ENVIRONMENT, message=message)


@app.route("/total")
def total():
    subtotal = float(request.args.get("subtotal", 0))
    code = request.args.get("code")
    return jsonify(total=calculate_total(subtotal, code))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
