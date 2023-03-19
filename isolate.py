import yfinance as yf
import datetime



aapl = yf.Ticker("AAPL").history(start = "2023-03-01", end= datetime.date.today(), interval="1d").at[str(datetime.date.today()), "Close"]
print(aapl)

# print(datetime.date.today())
