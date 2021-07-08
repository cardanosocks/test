import pandas as pd
import pandas_ta as ta
import yfinance as yf
import ccxt

exchange = ccxt.kraken()
bars =  exchange.fetch_ohlcv("GRT/USD")

# msft = yf.Ticker("MSFT")
# df = msft.history()
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
# adx = ta.adx(df['High'], df['Low'], df['Close'])
adx = df.ta.adx()
rsi = df.ta.rsi()
dm = df.ta.dm()
df = pd.concat([df, adx, rsi], axis=1)
print(df)
df = df[df['RSI_14'] < 30]
last_row = df.iloc[-1]

if last_row['ADX_14'] >= 25:
    
    if last_row['DMP_14'] > last_row['DMN_14']:
        msg = f"UPTREND IS EMERGING, the ADX is {last_row['ADX_14']:.2f}"
        print(msg)
    if last_row['DMN_14'] > last_row['DMP_14']:
        
        msg = f"DOWNTREND IS EMERGING, the ADX is {last_row['ADX_14']:.2f}, last price was {last_row['close']:.4f}"
        
        print(msg)
if last_row['ADX_14'] < 25:
    msg = f"NO CLEAR TREND APPARENT, the ADX is {last_row['ADX_14']:.2f}"
    print(msg)
    
payload = {
        'username': 'rich',
        'content': msg
    }
requests.post(webhook_url, json=payload)

#if last_row['ADX_14'] < 25:
 #   msg = f"NO CLEAR TREND: the ADX is {last_row['ADX_14']:.2f}"
  #  print(msg)

# df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume']) # Empty DataFrame

# Load data
# df = pd.read_csv("path/to/symbol.csv", sep=",")
# OR if you have yfinance installed
# df = df.ta.ticker(msft)

# VWAP requires the DataFrame index to be a DatetimeIndex.
# Replace "datetime" with the appropriate column from your DataFrame
# df.set_index(pd.DatetimeIndex(df["Date"]), inplace=True)
# df.set_index(df["Date"], inplace=True)
# Calculate Returns and append to the df DataFrame
# df.ta.log_return(cumulative=True, append=True)
 #df.ta.percent_return(cumulative=True, append=True)

