import nomics
nomics = nomics.Nomics("1fc83228c21c5dc0380e9c647d7ee91a")

res = nomics.Currencies.get_currencies(
    ids = ["BTC", "ETH"],
    interval = ["1d", "ytd"],
    convert = "EUR"
)

print(res)