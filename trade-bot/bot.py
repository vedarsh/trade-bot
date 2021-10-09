#ml functions
import math
import numpy
import plotly
import asyncio

#api functions
import yfinance as yf
from time import sleep
import plotly.graph_objects as go

class TradeInit:
    def __init__(self, ticker , eval_time = None):
        #initialising class elements
        self.eval_time = eval_time
        self.ticker = ticker
            #initialising yf api ticker
        self.tk = yf.Ticker(ticker)
            #default sleep time is 2.5s
        if eval_time is None:
            eval_time = 2500
    
    @property
    def information(self):
        #returns stock information including history
        return self.tk.info
    
    @property
    def max_volume(self):
        #returns total history for max time period
        return self.tk.history(period = "max")

if __name__ == "__main__":
    tick = TradeInit("TSLA") #placeholder "TSLA"
    print(tick.max_volume)   #returns max volume
