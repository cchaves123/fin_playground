# functions responsible for the extraction of data
# from an API, with various save methods (getter only)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import alpha_vantage.techindicators as ti
import alpha_vantage.cryptocurrencies as cc
import collections
import csv
import os
import time
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
print(today)

API_key = 'QMRK51DPGS5FK9UN'

#sp_names = pd.read_csv('constituents_csv.csv')
#sp_financials = pd.read_csv('constituents-financials_csv.csv')

ts = TimeSeries(key=API_key, output_format='pandas')
indicators = ti.TechIndicators(key=API_key, output_format='pandas')

def get_tickers():
    sp_names = pd.read_csv('constituents_csv.csv')
    ticker_symbols = [ sym for sym in sp_names.Symbol ]
    return ticker_symbols

def industry_dict():
    sp_financials = pd.read_csv('constituents-financials_csv.csv')
    sector_dict = {}
    for i,j in zip(sp_financials.Symbol, sp_financials.Sector):
        sector_dict[i] = j
    print(sector_dict['MMM'])
    return sector_dict

test, tmp_m = ts.get_daily('MMM', outputsize='full')
cols = ['open', 'high', 'low', 'close', 'volume']
print(test.head())





if __name__ == "__main__":
   print('suck me')
   get_tickers()
   industry_dict()

   
