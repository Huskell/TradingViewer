import pandas as pd


# def data_for_ploting(ticker):
#     parseFinam(str(ticker), 7)
#     data = pd.read_csv(ticker+'.txt')
#     return data


def candle_info(ticker):
    data = pd.read_csv('http://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{}/candles.csv?from=2020-05-1&interval=60'.format(str(ticker)),
                     sep=';', skiprows=[0])
    data.drop(['end', 'value'], axis=1, inplace=True)
    data['begin'] = pd.DatetimeIndex(data['begin'])
    data.set_index('begin', inplace=True)
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return data

