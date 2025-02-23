import http.client

from flask import Flask, jsonify

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def subtract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.subtract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        #if not util.validate_permissions(f"{num_1} * {num_2}", "user1"):
        #    return ("User has no permissions", http.client.FORBIDDEN, HEADERS)
        return ("{}".format(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    #except (TypeError, InvalidPermissions) as e:
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.divide(num_1, num_2)), http.client.OK, HEADERS)
    except ZeroDivisionError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.power(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    try:
        num = util.convert_to_number(op_1)
        return ("{}".format(CALCULATOR.sqrt(num)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/log10/<op_1>", methods=["GET"])
def log10(op_1):
    try:
        num = util.convert_to_number(op_1)
        return ("{}".format(CALCULATOR.log10(num)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

if __name__ == '__main__':
    api_application.run(debug=True)