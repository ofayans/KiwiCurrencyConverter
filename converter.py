#!/usr/bin/env python

from worker import do_job
from worker import deside

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--amount", help="Ulala")
parser.add_argument("--input_currency", help="Ulala")
parser.add_argument("--output_currency", help="Ulala")
args = parser.parse_args()

translate, icurrency = deside(args.input_currency)

print json.dumps(do_job(translate, args.amount,
                        icurrency,
                        args.output_currency))
