
from tiingo import TiingoClient
from pprint import pprint
import matplotlib.pyplot as plt

TIINGO_API_KEY = '6f5ad64cbd86511beca3ce3b91e61cbf031ae0a9'

config = {
    'api_key': TIINGO_API_KEY,
    'session': True # Reuse HTTP sessions across API calls for better performance
}

# Throughout the rest of this notebook, you'll use the "client" to interact with the Tiingo backend services.
client = TiingoClient(config)

# Get Ticker Metadata for the stock "GOOGL"
#ticker_metadata = client.get_ticker_metadata("GOOGL")
#pprint(ticker_metadata)

# THIS IS FOR JSON
if False:
    historical_prices = client.get_ticker_price("GOOGL",
                                            fmt='json',
                                            startDate='2019-06-01',
                                            endDate='2019-12-31',
                                            frequency='daily')
    pprint(historical_prices[:2])

#'btcusd'
df_btcusd = client.get_dataframe("btcusd",
                                            startDate='2019-06-01',
                                            endDate='2019-12-31',
                                            frequency='daily')

#'spy'
df_spy = client.get_dataframe("spy",
                                            startDate='2019-06-01',
                                            endDate='2019-12-31',
                                            frequency='daily')

#print(historical_prices_df.head(5))

columns_to_plot = ['adjClose']
df_btcusd_close = df_btcusd[columns_to_plot]
df_spy_close = df_spy[columns_to_plot]

fig1 = plt.figure()

color = 'tab:red'
ax1 = fig1.add_subplot()
ax1.plot(df_btcusd_close,color=color)


color = 'tab:blue'
ax2 = ax1.twinx()
ax2.plot(df_spy_close,color=color)


# columns_to_plot = ['adjClose']
# df_close = historical_prices_df[columns_to_plot] #.plot.line()
# df_close.plot()
plt.title('Bitcoin to SPY')
plt.show()

# the plot gets saved to 'output.png'
#plt.savefig('output.png')
