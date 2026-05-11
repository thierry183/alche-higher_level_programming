#!/usr/bin/python3
"""
math_utils.py
Author: MUHIRE
Date: May 2026

This module provides simple mathematical operations:
- addTwo: increases a number by 2
- multiply: multiplies two numbers
- magic_calculation: performs a custom calculation
- Calculator: a class that bundles these operations
"""

class Calculator:
    """
    A simple calculator class for basic math operations.

    Methods:
        addTwo(x): Increase a number by 2.
        multiply(a, b): Multiply two numbers.
        magic_calculation(a, b): Perform a custom calculation.
    """

    def addTwo(self, x):
        """
        Increase a number by 2.

        Parameters:
            x (int or float): The input number.

        Returns:
            int or float: The result of x + 2.
        """
        return x + 2

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.
        """
        return a * b

    def magic_calculation(self, a, b):
        """
        Perform a 'magic' operation:
        Add a and b, then multiply the result by 3.

        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The result of (a + b) * 3.
        """
        return (a + b) * 3

