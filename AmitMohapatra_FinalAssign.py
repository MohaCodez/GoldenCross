
from unittest import result
import matplotlib 
import backtrader as bt
import backtrader.analyzers as btanalyzers
import pandas as pd
import pandas_datareader
import os, argparse, sys
from strategies.GoldenCross import GoldenCross


cerebro = bt.Cerebro()
cerebro.broker.setcash(25000)

ADANIPOWER_prices = pd.read_csv('data\ADANIPOWER.csv', index_col = 'Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=ADANIPOWER_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)

cerebro.run()
cerebro.plot()
