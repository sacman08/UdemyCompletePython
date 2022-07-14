from typing import Dict, Any

import CalculatorApp


# Weclome
# What basic calc does
# ask for calc type (add, subtract, multipy, divide)
# perform math
# Return to calc type

def OurFunctions(entry, num1, num2):
    thisfunct = {
        'a': CalculatorApp.Calculator.add(num1, num2)
    }

    while entry != 'q':
        for key in thisfunct:
            thisfunct['{entry}']


print(
    """ Welcome to Basic Calculator!
    This app performs the four basic math functions:
    Add, Subtract, Multipy and Divide.
    """
)

entry = input('Please select function: "a" adds, "s" subtracts, "m" multiplies, "d" divides and "q" to quit:')
num1 = input('Enter first integer: ')
num2 = input('Enter second integer: ')

OurFunctions(entry)
