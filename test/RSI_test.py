# test/RSI_test.py


import unittest

# from buyholdsell.RSI import buyholdsell

# OBJECTIVE: test the buyholdsell() function from the buyholdsell/RSI.py file

def buyholdsell(n):
    """
    Param n is a number.
    Function will decide if the number is worth buying, holding, or selling.
    """

    if (n) in range(1, 30):
        return "I'm buying"
    elif (n) in range(30, 71):
        return "I'm holding"
    elif (n) in range(70, 101):
        return "I'm selling"
    else:
        return "Your number wasn't in the correct range"

class TestRSI(unittest.TestCase):
    
    def test_buyholdsell(self):
        """Test the output for condition"""
        n1 = 5
        n2 = 35
        n3 = 75
        self.assertEqual(buyholdsell(n1), "I'm buying")
        self.assertEqual(buyholdsell(n2), "I'm holding")
        self.assertEqual(buyholdsell(n3), "I'm selling")
        

if __name__ == "__main__":
    unittest.main()