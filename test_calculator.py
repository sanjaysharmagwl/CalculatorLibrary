""" Unit Test for calclulator """


import calculator


class Testcalculator():
    def test_addition(self):
        assert 4 == calculator.add(2,2)


    def test_subtraction(self):
        assert 2 == calculator.subtract(4,2)
