import math
import numpy
import plotly
import asyncio


import yfinance as yf
from time import sleep
import plotly.graph_objects as go

class TradeInit:
    def __init__(self, ticker , eval_time = None):
        #initialising class elements
        self.eval_time = eval_time
        self.ticker = ticker
        self.tk = yf.Ticker(ticker)
        if eval_time is None:
            eval_time = 2500
    
    @property
    def information(self):
        return self.tk.info
    
    @property
    def max_volume(self):
        return self.tk.history(period = "max")


if __name__ == "__main__":
    tick = TradeInit("TSLA")
    print(tick.max_volume)
