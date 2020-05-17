# predprep.py


# This is the coherent code for preparing data for predictions,
# the premise of the package which is separated into different
# modules for easier understanding and use by the user.

# Import Packages
import pandas as pd
import numpy as np


# Enter a CSV
print("Please, enter the URL of your CSV, without parentheses:")
df_url = input("")
# Example URL to be copy and pasted below as the input, or use your own
# BTC:
# https://query1.finance.yahoo.com/v7/finance/download/BTCUSD=X?period1=1279238400&period2=1588896000&interval=1d&events=history


# Import CSV from URL
df = pd.read_csv(df_url)


# Train/Test Split  ]
train = df[:int(df.shape[0] * 0.7)]
test = df[int(df.shape[0] * 0.7):]


def ttclean(X):
    """
    cleans data in train and test time series data frames
    """

    # Prevent SettingWithCopyWarning
    X = X.copy()

    # Add New Columns with Average Prices
    # This feature has previously had the most permutation importance
    X['HL Avg'] = (X['High'] + X['Low']) / 2  # High Low Average
    # Testing this new feature (made score worse, but has 3rd highest
    # permutation importance)
    X['OC Avg'] = (X['Open'] + X['Close']) / 2  # Open Close Average
    # Test another feature
    X['HL Range'] = abs((X['High'] - X['Low']))  # High Low Range
    # Another one
    X['OC Range'] = abs((X['Open'] - X['Close']))  # Open Close Range

    # Drop Date Column
    X = X.drop(columns=['Date'])

    # Return the clean data frames
    return X


# Apply the function to the train and test data frames
train = ttclean(train)
test = ttclean(test)


# Assign a target for predictive modeling
target = 'High'


# Arrange data into X features matrix and y target vector
X_train = train.drop(columns=target)
y_train = train[target]
X_test = test.drop(columns=target)
y_test = test[target]
