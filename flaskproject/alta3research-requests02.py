#!/usr/bin/env python3
import requests

from pprint import pprint
URL= "http://0.0.0.0:2224/data"

response = requests.get(URL).json()

print(response)