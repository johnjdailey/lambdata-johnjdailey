# df.py

import pandas as pd
import random

from buyholdsell.RSI import buyholdsell
from buyholdsell.ttclean import ttclean

print("HELLO WORLD")

df = pd.DataFrame({"Number": ["1", "30", "70", "100"]})
print(df.head())

print("-----------------")
x = random.randint(1, 101)
print("NUMBER", x)
print("Buy, hold, or sell?"), buyholdsell(x)  # invoking our function!!
