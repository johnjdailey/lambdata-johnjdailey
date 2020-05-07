# DF.py

import pandas
import random

from buyholdsell.RSI import buyholdsell

print("HELLO WORLD")

df = pandas.DataFrame({"Number": ["1", "30", "70", "100"]})
print(df.head())

print("-----------------")
x = random.randint(1, 101)
print("NUMBER", x)
print("Buy, hold, or sell?"), buyholdsell(x) # invoking our function!!