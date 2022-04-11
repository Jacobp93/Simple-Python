import plotly.offline as py
import plotly.graph_objs as go

from Binance_api import binance_price

table_trace = go.Table(
    domain=dict(x=[0, 0.5],
                y=[0, 1.0]),
    columnwidth=[30] + [33, 35, 33],
    columnorder=[0, 1, 2, 3, 4],
    header=dict(
        height=50,
        values=[['<b>Date</b>'], ['<b>Open Price</b>'], ['<b>High</b>'],
                ['<b>Low</b>'], ['<b>Close</b>'], ['<b>Volume</b>'], ['<b>Trade Number</b>']],
        line=dict(color='rgb(50,50,50)'),
        align=['left'] * 5,
        font=dict(color=['rgb(45,45,45)'] * 5, size=14),
        fill=dict(color='rgb(135,193,238)')
    ),
    cells=dict(values=[binance_price().index[:], binance_price()['open'], binance_price()['high'], binance_price()[
        'low'], binance_price()['close'], binance_price()['volume'], binance_price()['trades_number']]),
    line=dict(color='#106784'),
    align=['left'] * 5,
    font=dict(color=['rgb(45,45,45)'] * 5, size=12),
    format=[None] + [', .2f'] * 2 + [', .4f'],
    prefix=[None] * 2 + ['$', u'\u20BF'],
    suffix=[None] * 4,
    height=27,
    fill=dict(color=['rgb(135, 193, 238)', 'rgba(128 , 222, 249, 0.65)'])
)

fig = dict(data=[table_trace])
py.plot(fig, filename='table.html')
