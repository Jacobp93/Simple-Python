from binance.client import Client
import keys_api
from bs4 import BeautifulSoup as soup

client = Client(api_key=keys_api.Pkey, api_secret=keys_api.Skey)

##avg_price = client.get_avg_price(symbol='BTCBUSD')

exe = client.get_avg_price(symbol='BTCBUSD')

print(exe)
