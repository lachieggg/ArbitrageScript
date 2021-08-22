#!/usr/bin/env python3

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
from os import getenv
from json import loads

load_dotenv()

API_KEY = getenv('api_key')
API_URL = getenv('api_url')
API_ROUTE = getenv('api_route')
if not API_URL.startswith('https://'):
    exit('\nError: api_url must begin with protocol (eg. https)')


route = '/v1/cryptocurrency/listings/latest'

url = API_URL + route

parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


# ...
# ...
