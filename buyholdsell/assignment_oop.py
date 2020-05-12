from pandas import DataFrame

# State abbreviation -> Full Name and vice versa. Fl -> Florida, etc.

class DataProcessor():
    def __init__(self, something_else): # was originally my_df, doesn't matter
        """
        Params: my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations.
        """
        self.df = something_else # was originally my_df, doesn't matter

    def add_state_names(self): # was originally my_df, doesn't matter
        """
        Adds a column of state names to accompany and corresponding column of state abbreviations.
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        # type(my_df["abbrev"]) # -> pandas.core.series.Series'
        self.df["name"] = self.df["abbrev"].map(names_map)


if __name__ == '__main__':

    df = DataFrame({"abbrev": ["CA", "CO", "CT"]})

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names(df)
    print(prcoessor.df.head())
