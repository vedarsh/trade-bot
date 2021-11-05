#api functions
import yfinance as yf
from numpy import array
import requests

api_url = "https://www.google.com/finance/"

class LiveInfo:
    def __init__(self, api_url, market_name = None):
        self.api_url = api_url
        self.market_name = market_name
        if market_name is None:
            market_name = "NYSE"
        self.request = request.get(api_url)

    @property
    def fetch_current():
        return self.r.text


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
    return tick.information
    return tick.max_volume


print(debug("tsla"))

