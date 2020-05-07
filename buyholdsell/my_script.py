# my_script.py

import pandas

from my_mod import buyholdsell

print("HELLO WORLD")

df = pandas.DataFrame({"Number": ["5", "25", "75", "95"]})
print(df.head())

print("-----------------")
x = 5
print("NUMBER", x)
print("Buy, hold, or sell?"), buyholdsell(x) # invoking our function!!