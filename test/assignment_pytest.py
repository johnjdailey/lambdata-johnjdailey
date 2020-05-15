# test/assignment_pytest.py

from pandas import DataFrame

from buyholdsell.assignment import add_state_names

# OBJECTIVE: test the add_state_names() function from the buyholdsell/assignment.py file

def test_add_state_names():
    # expect that it has one more column and the same number of rows, after we invoke the function
    # expect that certain column names exist before and certain col names exist after
    
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    #self.assertEqual(list(df.columns), ['abbrev'])
    assert list(df.columns) == ['abbrev']
    
    result = add_state_names(df)
    #self.assertEqual(list(result.columns), ["abbrev", "name"])
    #self.assertEqual(result.iloc[0]["abbrev"], "CA")
    #self.assertEqual(result.iloc[0]["name"], "Cali")
    assert list(result.columns) == ["abbrev", "name"]
    assert result.iloc[0]["abbrev"] == "CA"
    assert result.iloc[0]["name"] == "Cali"
