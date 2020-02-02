import requests
import json

from sqlite_utils import Database
import sqlite3

url = "https://bravenewcoin-v1.p.rapidapi.com/ticker"

querystring = {"show":"usd","coin":"btc"}

headers = {
    'x-rapidapi-host': "bravenewcoin-v1.p.rapidapi.com",
    'x-rapidapi-key': "2b9d949e28msh7079164c2f9c012p1d5ba2jsnb17a5e089c30"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

mydict = json.loads(response.text)

# https://sqlite-utils.readthedocs.io/en/stable/python-api.html#connecting-to-or-creating-a-database
db = Database(sqlite3.connect("sqlite/apidata.db"))
bravenewcoin = db["bravenewcoin"]
bravenewcoin.insert(mydict)


#pretty_json = json.loads(response.text)
#print (json.dumps(pretty_json, indent=2))

print(db.table_names())

#print(response.text)

# dogs.insert({
#     "name": "Cleo",
#     "twitter": "cleopaws",
#     "age": 3,
#     "is_good_dog": True,
# })


# look at later: https://min-api.cryptocompare.com/