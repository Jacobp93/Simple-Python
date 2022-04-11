from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from os import pipe
import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
from sklearn import cluster
from sklearn import pipeline
from yahoo_fin import stock_info as si


company_tickers = ['AAPL', 'FB', 'NVDA', ]

clusters = 3

start = dt.datetime.now() - dt.timedelta(days=365 * 2)
end = dt.datetime.now()

data = web.DataReader(list(company_tickers), 'yahoo', start, end)

open_values = np.array(data['Open'].T)
close_values = np.array(data['Close'].T)

daily_movement = close_values - open_values

normalizer = Normalizer()

clustering_model = KMeans(n_clusters=clusters, max_iter=1000)
pipeline = make_pipeline(normalizer, clustering_model)
pipeline.fit(daily_movement)
clusters = pipeline.predict(daily_movement)

results = pd.DataFrame({

    'clusters': clusters,
    'tickers': list(company_tickers)}).sort_values(by=['clusters'], axis=0)

print(results)
