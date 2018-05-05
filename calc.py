#! /usr/bin/python3
""""""

import argparse
import math


# , 'acos': <built-in function acos>, 'acosh': <built-in function acosh>, 'asin': <built-in function asin>, 'asinh': <built-in function asinh>, 'atan': <built-in function atan>, 'atan2': <built-in function atan2>, 'atanh': <built-in function atanh>, 'ceil': <built-in function ceil>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'cosh': <built-in function cosh>, 'degrees': <built-in function degrees>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'expm1': <built-in function expm1>, 'fabs': <built-in function fabs>, 'factorial': <built-in function factorial>, 'floor': <built-in function floor>, 'fmod': <built-in function fmod>, 'frexp': <built-in function frexp>, 'fsum': <built-in function fsum>, 'gamma': <built-in function gamma>, 'gcd': <built-in function gcd>, 'hypot': <built-in function hypot>, 'isclose': <built-in function isclose>, 'isfinite': <built-in function isfinite>, 'isinf': <built-in function isinf>, 'isnan': <built-in function isnan>, 'ldexp': <built-in function ldexp>, 'lgamma': <built-in function lgamma>, 'log': <built-in function log>, 'log1p': <built-in function log1p>, 'log10': <built-in function log10>, 'log2': <built-in function log2>, 'modf': <built-in function modf>, 'pow': <built-in function pow>, 'radians': <built-in function radians>, 'sin': <built-in function sin>, 'sinh': <built-in function sinh>, 'sqrt': <built-in function sqrt>, 'tan': <built-in function tan>, 'tanh': <built-in function tanh>, 'trunc': <built-in function trunc>, 'pi': 3.141592653589793, 'e': 2.718281828459045, 'tau': 6.283185307179586, 'inf': inf, 'nan': nan}
math_dict = {

}


class MyError(Exception):
    """class of error with message"""
    def __init__(self, message):
        self.message = message


def validate(exp):
    exp = exp.replace(' ', '')
    if len(exp) < 3:
        raise MyError("Not full expression")
    if exp.count("(") != exp.count(")"):
        raise MyError("Brackets are not balanced")

    return exp


def parse_command_line_args():
    """function to parse command line arguments"""
    parser = argparse.ArgumentParser(description="Pure-python command-line calculator.")
    parser.add_argument("EXPRESSION", help="expression string to evaluate")
    parser.add_argument("-m", '--module', nargs='+', help="additional modules to use")
    arguments = parser.parse_args()
    return arguments


class Arithmetic:
    """Arithmetic operations class
    Methods:
        add(x, y) - adds values on either side of the operator(x + y)
        subtruct(x, y) - subtracts right hand operand from left hand operand(x - y)
        multiply(x, y) - multiplies values on either side of the operator(x * y)
        divide(x, y) - divides left hand operand by right hand operand(x / y)
        floor_divide(x, y) - the division of operands where the result is the quotient
                             in which the digits after the decimal point are removed.
                             But if one of the operands is negative, the result is floored,
                             i.e., rounded away from zero (x // y)
        remainder(x, y) - divides left hand operand by right hand operand and returns remainder(x % y)
        power(x, y) - performs exponential (power) calculation on operators(x ** y)
        """
    @staticmethod
    def add(x, y):
        """Adds values on either side of the operator(x + y)"""
        return x + y

    @staticmethod
    def subtruct(x, y):
        """Subtracts right hand operand from left hand operand(x - y)"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiplies values on either side of the operator(x * y)"""
        return x * y

    @staticmethod
    def divide(x, y):
        """Divides left hand operand by right hand operand(x / y)"""
        return x / y

    @staticmethod
    def floor_divide(x, y):
        """Floor division(x // y)"""
        return x // y

    @staticmethod
    def remainder(x, y):
        """Divides left hand operand by right hand operand and returns remainder(x % y)"""
        return x % y

    @staticmethod
    def power(x, y):
        """Performs exponential (power) calculation on operators(x ** y)"""
        return x ** y


class Comparison:

    @staticmethod
    def little(x, y):
        return x < y

    @staticmethod
    def little_or_equal(x, y):
        return x <= y

    @staticmethod
    def equal(x, y):
        return x == y

    @staticmethod
    def not_equal(x, y):
        return x != y

    @staticmethod
    def bigger_or_equal(x, y):
        return x >= y

    @staticmethod
    def bigger(x, y):
        return x > y


class BuiltIns:

    @staticmethod
    def abs_value(x):
        return abs(x)

    @staticmethod
    def get_power(x, y, z=None):
        return pow(x, y, z=z)

    @staticmethod
    def make_round(x, y=0):
        return round(x, ndigits=y)


if __name__ == "__main__":
    args = parse_command_line_args()
    try:
        data = validate(args.EXPRESSION)
        print('[DEBUG] exp:', data)

    except MyError as e:
        print("Error: {0}".format(e))
