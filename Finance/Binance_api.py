from binance.client import Client  # binance-Python
from datetime import datetime
from pandas import DataFrame as df

import keys_api


def binance_price():

    client = Client(api_key=keys_api.Pkey, api_secret=keys_api.Skey)
    # ^^ api keys from another py file
    candles = client.get_klines(
        symbol='BTCBUSD', interval=Client.KLINE_INTERVAL_1HOUR
    )
    candles_data_frame = df(candles)
    candles_data_frame_date = candles_data_frame[0]  # index
    final_date = []
    for time in candles_data_frame_date.unique():
        # coverts 500 rows = 20 days from 500 hours
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)
        # ^^ converts INT / binance date time which is set by milliseconds so this conversion makes it into a real date

    candles_data_frame.pop(0)
    candles_data_frame.pop(11)
    dataframe_final_date = df(final_date)
    dataframe_final_date.columns = ['date']  # - Adds a column as "Date"
    final_dataframe = candles_data_frame.join(
        dataframe_final_date)  # joining settings for table
    final_dataframe.set_index('date', inplace=True)
    final_dataframe.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time',
                               'asset_volume', 'trades_number', 'taker_buy_base', 'taker_buy_qoute']  # column names for table
    return final_dataframe


print(binance_price())
