# readnsplit.py



# Import
import pandas as pd


# Enter a CSV
print("Please, enter the URL of your CSV, without parentheses:")
df_url = input("")
# Example URL to be copy and pasted below as the input, or use your own
# BTC: https://query1.finance.yahoo.com/v7/finance/download/BTCUSD=X?period1=1279238400&period2=1588896000&interval=1d&events=history


# Import CSV from URL
df = pd.read_csv(df_url)


# Train/Test Split  ] 
train = df[:int(df.shape[0]*0.7)]
test = df[int(df.shape[0]*0.7):]
