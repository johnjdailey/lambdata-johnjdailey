# tsclean.py


# Import Packages
import pandas as pd
import numpy as np


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


def tsclean(X):


        """ 
        cleans data in train and test time series data frames
        """

        # Prevent SettingWithCopyWarning
        X = X.copy()

        # Consider code to remove or replace extreme outliers
        # ...

        # When columns have zeros and shouldn't, they are like null values.
        # So we will replace the zeros with nulls, and impute missing values later.
        # Also create a "missing indicator" column, because the fact that
        # values are missing may be a predictive signal.

        # cols_with_zeros = X[(X == 0).all(1)]
        # for col in cols_with_zeros:
        #     X[col] = X[col].replace(0, np.nan)
        #     X[col+'_MISSING'] = X[col].isnull()

        # Or just drop Null/NaN values.
        # X = X.dropna()

        # Make new df without 0's.
        # X = X.loc[(X != 0).all(1)]

        # Drop duplicate rows
        # X = X.drop_duplicates

        # Add New Columns with Average Prices
        # This feature has previously had the most permutation importance
        X['HL Avg'] = (X['High'] + X['Low'])/2 # High Low Average
        # Testing this new feature (made score worse, but has 3rd highest permutation importance)
        X['OC Avg'] = (X['Open'] + X['Close'])/2 # Open Close Average
        # Test another feature
        X['HL Range'] = abs((X['High'] - X['Low'])) # High Low Range
        # Another one
        X['OC Range'] = abs((X['Open'] - X['Close'])) # Open Close Range

        # Drop duplicate columns
        # X = X[:,~X.columns.duplicated()]
        # 'function' object has no attribute 'columns'

        # Drop unusable variance
        # unusable_variance = []
        # X = X.drop(columns=unusable_variance)

        # Convert date to datetime
        # X['Date'] = pd.to_datetime(X['Date'], infer_datetime_format=True)
        # TypeError: 'method' object is not subscriptable

        # Extract components from Date, then drop the original column
        # X['Year'] = X['Date'].dt.year
        # X['Month'] = X['Date'].dt.month
        # X['Day'] = X['Date'].dt.day
        X = X.drop(columns=['Date'])

        # Return the clean data frames
        return X

# Apply the function to the train and test data frames
train = tsclean(train)
test = tsclean(test)

# Assign a target for predictive modeling
target = 'High'

# Arrange data into X features matrix and y target vector
X_train = train.drop(columns=target)
y_train = train[target]
X_test = test.drop(columns=target)
y_test = test[target]

print(X_train.head())
