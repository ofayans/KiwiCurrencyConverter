#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from worker import do_job
from flask import jsonify
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)


def returnError(missing_arg, error):
    error.description = ("Your request lacks the obligatory argument: %s"
                         % missing_arg)
    return error


@app.route("/")
def main():
    amount = None
    icurrency = None
    ocurrency = None
    try:
        amount = request.args['amount']
    except BadRequestKeyError as e:
        return returnError('amount', e)
    try:
        icurrency = request.args['input_currency']
    except BadRequestKeyError as e:
        return returnError('input_currency', e)
    try:
        ocurrency = request.args['output_currency']
    except BadRequestKeyError:
        pass
    return jsonify(do_job(float(amount), icurrency, ocurrency))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
