from pandas import DataFrame

# State abbreviation -> Full Name and vice versa. Fl -> FLorida, etc.


def add_state_names(my_df):
    """
    Adds a column of state names to accompany a corresponding column of state abbreviations.

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations.

    Returns:
        copy of the original dataframe, with another column
    """
    # TODO: add a column of corresponding state names
    # dict with abbrev/name mappings
    # create a new column that is a copy of the first, but mapped with the names
    # concat with axis =1

    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
    # type(my_df["abbrev"]) # -> pandas.core.series.Series'

    new_df["name"] = new_df["abbrev"].map(names_map)

    return new_df


if __name__ == '__main__':

    df = DataFrame({"abbrev": ["CA", "CO", "CT"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2)
