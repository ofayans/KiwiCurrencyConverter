#!/usr/bin/env python

from currency_converter import CurrencyConverter
from currency_converter.currency_converter import RateNotFoundError
import json
import os


def translate_symbol(symbol, web=True):
    file_path = os.path.dirname(os.path.abspath(__file__))
    if not web:
        symbol = symbol.decode('utf-8')
    with open(file_path+'/raw_data/currencies.json') as f:
        currency_data = json.load(f)
        try:
            return filter(lambda x: x[u'symbol'] == symbol,
                          currency_data)[0][u'cc']
        except IndexError:
            # It was a currency code, not symbol
            return symbol


def do_job(amount, icurrency, ocurrency=None, web=True):
    converter = CurrencyConverter()
    icurrency = translate_symbol(icurrency, web)
    result = {}
    result['input'] = {"amount": amount,
                       "currency": icurrency}
    if ocurrency:
        ocurrency = translate_symbol(ocurrency)
        result['output'] = {ocurrency: converter.convert(amount,
                                                         icurrency,
                                                         ocurrency)}
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
