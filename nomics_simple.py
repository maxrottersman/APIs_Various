
from pathlib import Path
import requests
from pprint import pprint
import sys

scriptPath = Path(__file__).parent
keyfile = scriptPath / 'licenses.txt'

urlbase = 'https://api.nomics.com/v1/currencies/ticker?key='
key = Path(keyfile).read_text()
urlparams = '&ids=BTC&interval=1h&convert=USD'


test1 = ("https://api.nomics.com/v1/supplies/history?key=1fc83228c21c5dc0380e9c647d7ee91a&currency=BTC&start=2020-01-01T00&end=2020-01-02T00")

#=importdata("https://api.nomics.com/v1/prices?key=2018-09-demo-dont-deploy-b69315e440beb145&format=csv")

#curl "https://api.nomics.com/v1/currencies/ticker?key=1fc83228c21c5dc0380e9c647d7ee9&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR"

r = requests.get(urlbase+key+urlparams)
#r = requests.get(test1)

#print(r)
pprint(r.json())