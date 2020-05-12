from pandas import DataFrame

# State abbreviation -> Full Name and vice versa. Fl -> Florida, etc.

class MyFrame(DataFrame):

    def add_state_names(self): # was originally my_df, doesn't matter
        """
        Adds a column of state names to accompany and corresponding column of state abbreviations.
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self["name"] = self["abbrev"].map(names_map)

if __name__ == '__main__':

    my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "CT", "DC", "TX"]})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())
