# ttclean.py



def ttclean(X):


        """ 
        cleans data in train and test time series data frames
        """


        # Prevent SettingWithCopyWarning
        X = X.copy()


        # Add New Columns with Average Prices
        # This feature has previously had the most permutation importance
        X['HL Avg'] = (X['High'] + X['Low'])/2 # High Low Average
        # Testing this new feature (made score worse, but has 3rd highest permutation importance)
        X['OC Avg'] = (X['Open'] + X['Close'])/2 # Open Close Average
        # Test another feature
        X['HL Range'] = abs((X['High'] - X['Low'])) # High Low Range
        # Another one
        X['OC Range'] = abs((X['Open'] - X['Close'])) # Open Close Range


        # Drop Date Column
        X = X.drop(columns=['Date'])


        # Return the clean data frames
        return X
