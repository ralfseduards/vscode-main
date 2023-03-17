import yfinance as yf


ticker = "AAPl"

data = yf.Ticker(ticker)


dataframe = data.history(period='5d', interval = "1h")

print(dataframe)
# print(data.info)