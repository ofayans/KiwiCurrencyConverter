#!/usr/bin/env python

from currency_converter import CurrencyConverter
from currency_converter.currency_converter import RateNotFoundError
import json
import os


def translate_symbol(symbol):
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+'/raw_data/currencies.json') as f:
        currency_data = json.load(f)
        import pdb
        pdb.set_trace()
        return filter(lambda x: x[u'symbol'] == symbol, currency_data)[0][u'cc']
    return None


def deside(symbol):
    result = symbol.decode('utf-8')
    if result:
        return result, True
    return symbol, False 


def do_job(translate, amount, icurrency, ocurrency=None):
    converter = CurrencyConverter()
    if translate:
        icurrency = translate_symbol(icurrency)
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
    return result


