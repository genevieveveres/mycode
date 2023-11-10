#!/usr/bin/env python3
import requests
import json
from pprint import pprint
URL= "http://0.0.0.0:2224/"

response = requests.get(URL + "data").json()

pprint(response)