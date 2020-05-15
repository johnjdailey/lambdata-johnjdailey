# test/dataprocessor_test.py


import unittest
from pandas import DataFrame

from buyholdsell.assignment_oop import DataProcessor

class TestDataProcessor(unittest.TestCase):
    
    def test_add_state_names_oop(self):
        # expect that it has one more column and the same number of rows, after we invoke the function
        # expect that certain column names exist before and certain col names exist after
        
        df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        
        processor.add_state_names()
        
        self.assertEqual(list(processor.df.columns), ["abbrev", "name"])
        self.assertEqual(processor.df.iloc[0]["abbrev"], "CA")
        self.assertEqual(processor.df.iloc[0]["name"], "Cali")

if __name__ == "__main__":
    unittest.main()