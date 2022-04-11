import yfinance as yf
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

plt.style.use("dark_background")

crypto = ['BTC', 'ETH', 'XRP', 'AVAX']
amounts = [20, 15, 50, 20]
values = [si.get_live_price(crypto[i]) * amounts[i]
          for i in range(len(crypto))]
sectors = [yf.Ticker(x).get_info()['industry'] for x in crypto]
countries = [yf.Ticker(x).get_info()['country'] for x in crypto]
market_cap = [yf.Ticker(x).get_info()['marketcap'] for x in crypto]


print(yf.Ticker("").get_info())
