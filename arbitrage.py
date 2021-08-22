#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('api_key')

print(API_KEY)
