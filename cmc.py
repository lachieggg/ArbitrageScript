#!/usr/bin/env python3

from dotenv import load_dotenv
from os import getenv
from json import dumps

import coinmarketcapapi

load_dotenv()

API_KEY = getenv('api_key')
API_CURRENCY = getenv('api_currency')
API_SYMBOLS = getenv('api_symbols')

cmc = coinmarketcapapi.CoinMarketCapAPI(API_KEY)

def get_price_from_data(data, symbol):
    q = data.get(symbol)
    q = q.get('quote')
    q = q.get(API_CURRENCY)
    q = q.get('price')

    return q

def main():
    if not API_KEY or not API_CURRENCY or not API_SYMBOLS:
        exit('\nError: at least one of the environment variables is not set')

    try:
        response = cmc.cryptocurrency_quotes_latest(symbol=API_SYMBOLS)
        data = response.data
        quotes = {}
        for symbol in data:
            quotes[symbol] = get_price_from_data(data, symbol)
        print(dumps(quotes, indent=4))

    except coinmarketcapapi.CoinMarketCapAPIError as e:
        message = str(e) + "\nExiting..."
        exit(message)

    except Exception as e:
        exit(e)

if(__name__ == "__main__"):
    main()