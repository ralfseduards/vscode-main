import yfinance as yf
import datetime

class Stock:
    def __init__(self, ticker, price = 10):
        self.ticker = ticker
        self.buy_price = price
        # self.price = price
        # self.price = yf.Ticker(self.ticker).history(start = "2023-03-01", end= datetime.date.today(), interval="1d")["Close"][-1]
    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        if value.islower():
            value = value.upper()
        self._ticker = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self):
        self._price = int(yf.Ticker(self.ticker).history(start = "2023-03-01", end= datetime.date.today(), interval="1d").at(-1 , "Close"))

class Portfolio:
    def __init__(self, stocks:list,):
        self.stocks = [Stock(x).ticker for x in stocks]

    def get_value(self):
        return sum([Stock(stock).price for stock in self.stocks])

    


apple = Stock("appl")
print(apple.ticker)
print(apple.price)

# aapl = yf.Ticker("AAPL").history(start = "2023-03-01", end= datetime.date.today(), interval="1d")["Close"][-1]
# print(aapl)



# get ticker
# get current price !!!
# get future  price ???

#  MAKE A PORTFOLIO
# 