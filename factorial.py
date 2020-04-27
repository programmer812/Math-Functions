# Factorial
# 0! = 1
# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6

# n! = n * n - 1 * n - 2 ...

import unittest

def factorial(n):
    '''Finding the factorial of a number, n'''
    if type(n) != int:
        return "'n' must be an integer"
    elif n < 0:
        return "Cannot find factorial of negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def test_basic(self):
        testcase = 5
        expected = 120
        self.assertEqual(factorial(testcase), expected)
    def test_basic_2(self):
        testcase = 10
        expected = 3628800
        self.assertEqual(factorial(testcase), expected)
    def test_edge_1(self):
        testcase = -5
        expected = "Cannot find factorial of negative number"
        self.assertEqual(factorial(testcase), expected)
    def test_edge_2(self):
        testcase = "abc"
        expected = "'n' must be an integer"
        self.assertEqual(factorial(testcase), expected)

unittest.main()
