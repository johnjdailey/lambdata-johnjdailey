# test/RSI_test.py


import unittest

from buyholdsell.RSI import buyholdsell

# OBJECTIVE: test the buyholdsell() function from the buyholdsell/RSI.py file

class TestRSI(unittest.TestCase):
    
    def test_buyholdsell(self):
        # expect that it prints the correct statement for the correct range
        self.assertTrue(buyholdsell(1), 1)
        
        # https://docs.python.org/3/library/exceptions.html#ValueError
        with self.assertRaises(ValueError):
            buyholdsell(101)
        
        with self.assertRaises(ValueError):
            buyholdsell(0)

if __name__ == "__main__":
    unittest.main()