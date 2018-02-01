#!/usr/bin/env python

from currency_converter import CurrencyConverter
from currency_converter.currency_converter import RateNotFoundError
import json

def do_job(amount, icurrency, ocurrency=None):
    converter = CurrencyConverter()
    result = {}
    result['input'] = { "amount": amount,
                        "currency": icurrency}
    if ocurrency:
        result['output'] = {ocurrency: converter.convert(amount, icurrency, ocurrency)}
    else:
        destination_currencies = converter.currencies - set([icurrency])
        output = {}
        for i in destination_currencies:
            try:
                output[i] = converter.convert(amount, icurrency, i)
            except RateNotFoundError:
                pass
        result['output'] = output
    print json.dumps(result)


