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


if __name__ == "__main__":
    trd = TradeInit("TSLA")
    print(trd.information)
