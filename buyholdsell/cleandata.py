# cleandata.py

def cleandata(x):

    import pandas as pd
    import numpy as np

    """ 
    cleans data in dataframes
    
    x is a dataframe
    """

    # Prevent SettingWithCopyWarning
    X = X.copy()

    # Consider code to remove or replace extreme outliers
    #...

    # When columns have zeros and shouldn't, they are like null values.
    # So we will replace the zeros with nulls, and impute missing values later.
    # Also create a "missing indicator" column, because the fact that
    # values are missing may be a predictive signal.
    
    # cols_with_zeros = X[(X == 0).all(1)]
    # for col in cols_with_zeros:
    #     X[col] = X[col].replace(0, np.nan)
    #     X[col+'_MISSING'] = X[col].isnull()

    # Or just drop Null/NaN values.
    X = X.dropna()

    # Make new df without 0's.
    X = X[(X != 0).all(1)]

    # Drop duplicate rows
    X = X.drop_duplicates

    # Drop duplicate columns
    X = X.loc[:,~X.columns.duplicated()]

    # Drop unusable variance
    unusable_variance = []
    X = X.drop(columns=unusable_variance)

    # Convert date to datetime
    X['Date'] = pd.to_datetime(X['Date'], infer_datetime_format=True)

    # Extract components from Date, then drop the original column
    X['Year'] = X['Date'].dt.year
    X['Month'] = X['Date'].dt.month
    X['Day'] = X['Date'].dt.day
    X = X.drop(columns='Date')

    # Return the wrangle dataframe

    train = cleandata(train)
    val = cleandata(val)
    test = cleandata(test)
