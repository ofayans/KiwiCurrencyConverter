#!/usr/bin/env python
# -*- coding: utf-8 -*-
from worker import do_job

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--amount", help="""Amount of currency you want to
                    exchange, a float""")
parser.add_argument("--input_currency", help="""Name of currency you want to
                    exchange. May be either a three-letter code or a symbol,
                    i. e. both GBP and £ are acceptable""")
parser.add_argument("--output_currency", help="""Name of targetr currency. Same
                    rules as for input_currency. This is an optional parameter.
                    If you do not provide it, the result will be shown for all
                    other currencies""")
args = parser.parse_args()

if args.amount is None:
    exit("Please provide '--amount' parameter")
if args.input_currency is None:
    exit("Please provide '--input_currency' parameter")

print json.dumps(do_job(args.amount,
                        args.input_currency,
                        args.output_currency, web=False))
