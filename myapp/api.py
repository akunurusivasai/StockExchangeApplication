from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import matplotlib.pyplot as plt
import pandas as  pd
import time
import yfinance as yf

ts = TimeSeries(key='SQJ79Z6XSGMB82UO', output_format='pandas')
ts1 = TimeSeries(key='JE28RV66FYGJAQ07', output_format='pandas')


def details(sym):
    data, meta_data = ts.get_quote_endpoint(symbol=sym)
    return Details(s=data['01. symbol'][0], o=data['02. open'][0],
                   h=data['03. high'][0], l=data['04. low'][0],
                   p=data['05. price'][0], v=data['06. volume'][0],
                   lt=data['07. latest trading day'][0], pc=data['08. previous close'][0],
                   c=data['09. change'][0], cp=data['10. change percent'][0])


class Details:
    def __init__(self, s, o, h, l, p, v, lt, pc, c, cp):
        self.s = s
        self.o = o
        self.h = h
        self.l = l
        self.p = p
        self.v = v
        self.lt = lt
        self.pc = pc
        self.c = c
        self.cp = cp


def finance(sym, p):
    s = yf.Ticker(sym)
    print(sym, p)
    if p == '1d':
        s = s.history(period='1d', interval='30m')
    elif p == '5d':
        s = s.history(period='5d', interval='1d')
    elif p == '1mo':
        s = s.history(period='1mo', interval='1d')
    elif p == '6mo':
        s = s.history(period='6mo', interval='1wk')
    elif p == '1y':
        s = s.history(period='1y', interval='1mo')
    elif p == '5y':
        s = s.history(period='5y', interval='3mo')
    else:
        s = s.history(period='max', interval='3mo')
    price = []
    index = []
    s = s.dropna()
    for i in range(len(s.index)):
        price.append(s['Open'][i])
        index.append(str(s.index[i]))

    return price, index
