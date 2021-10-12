#api functions
import yfinance as yf
from numpy import array

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

    @property
    def quarterly_earnings(self):
        #returns quarterly earnings
        return self.tk.quarterly_earnings
    
    @property
    def sustain(self):
        #returns sustainability
        return self.tk.sustainability

def debug(name):
    tick = TradeInit(name) #placeholder "TSLA"
    print(tick.max_volume)
    print(tick.quarterly_earnings)
    return tick.information

print(debug("tsla"))

