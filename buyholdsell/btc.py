import pandas as pd
import numpy as np
from buyholdsell.tsclean import tsclean

btc_url = "https://query1.finance.yahoo.com/v7/finance/download/BTCUSD=X?period1=1279238400&period2=1588896000&interval=1d&events=history"

df = pd.read_csv(btc_url)

tsclean(df)

(train.shape, test.shape)