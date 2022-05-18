# pip install plotly
# pip install pandas_datareader

import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web

start = datetime.datetime(2020, 1, 1)  # time frames for data (YY MM DD)
end = datetime.datetime(2020, 6, 4)


# api details --- update ticker below to alter api call
XRP = web.DataReader('XRP-USD', 'yahoo', start, end)
BTC = web.DataReader('BTC-USD', 'yahoo', start, end)
ETH = web.DataReader('ETH-USD', 'yahoo', start, end)


trace = go.Ohlc(
    x=XRP.index[:],
    open=XRP['Open'],
    high=XRP['High'],
    low=XRP['Low'],
    close=XRP['Close'],
    name='XRP',
    increasing=dict(line=dict(color='green')),
    # You can change the colours of the graph green = increase
    decreasing=dict(line=dict(color='red')),  # red = decrease
)

trace2 = go.Ohlc(
    x=BTC.index[:],
    open=BTC['Open'],
    high=BTC['High'],
    low=BTC['Low'],
    close=BTC['Close'],
    name='BTC',
    increasing=dict(line=dict(color='green')),
    decreasing=dict(line=dict(color='red')),

)

trace3 = go.Ohlc(
    x=ETH.index[:],
    open=ETH['Open'],
    high=ETH['High'],
    low=ETH['Low'],
    close=ETH['Close'],
    name='ETH',
    increasing=dict(line=dict(color='green')),
    decreasing=dict(line=dict(color='red')),
)

data = [trace, trace2, trace3]
layout = {
    'title': 'BTC vs ETH vs XRP',
    'yaxis': {'title': 'Price per stock'}
}

fig = dict(data=data, layout=layout)
py.plot(fig, filename='cryptoprices.html')
