import yfinance as yf
import datetime

class Stock:
    def __init__(self, ticker, price = 10):
        self.ticker = ticker
        # self.price = price
        self.price = yf.Ticker(self.ticker).regular_market_previous_close()
    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        if value.islower():
            value = value.upper()
        self._ticker = value

class Portfolio:
    def __init__(self, stocks:list,):
        self.stocks = [Stock(x).ticker for x in stocks]

    def get_value(self):
        return sum([Stock(stock).price for stock in self.stocks])

    


apple = Stock("appl")
print(apple.ticker)
print(apple.price)

# port = Portfolio(["aapl", "u", "pypl", "tsla"])
# print(port.stocks)
# print(port.get_value())
print(datetime.date.today())

# get ticker
# get current price !!!
# get future  price ???

#  MAKE A PORTFOLIO
# 