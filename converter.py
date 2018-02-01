#!/usr/bin/env python

from worker import do_job
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--amount", help="Ulala")
parser.add_argument("--input_currency", help="Ulala")
parser.add_argument("--output_currency", help="Ulala")
args = parser.parse_args()

do_job(args.amount, args.input_currency, args.output_currency)
