#!/usr/bin/env python

from flask import Flask
from flask import request
from worker import do_job
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def main():
    amount = request.args['amount']
    icurrency = request.args['input_currency']
    ocurrency = request.args['output_currency']
#    import pdb
#    pdb.set_trace()
    return jsonify(do_job(float(amount), icurrency, ocurrency))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
