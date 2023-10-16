# Write a Fraction class to represent rational numbers like 1/2 and -3/8.
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = gcd(numerator, denominator)
        self.__numerator = numerator // common
        self.__denominator = denominator // common

        # Determine the sign of the fraction
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __add__(self, other):
        new_numerator = self.__numerator * other.get_denominator() + self.__denominator * other.get_numerator()
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.__numerator * other.get_denominator() - self.__denominator * other.get_numerator()
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.__numerator * other.get_numerator()
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.get_numerator() == 0:
            raise ValueError("Division by zero is not allowed.")
        new_numerator = self.__numerator * other.get_denominator()
        new_denominator = self.__denominator * other.get_numerator()
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

# Example Usage
fraction1 = Fraction(1, 2)
fraction2 = Fraction(-3, 8)

# Addition
result_addition = fraction1 + fraction2
print("Addition:", result_addition)  # Output: 1/8

# Subtraction
result_subtraction = fraction1 - fraction2
print("Subtraction:", result_subtraction)  # Output: 5/8

# Multiplication
result_multiplication = fraction1 * fraction2
print("Multiplication:", result_multiplication)  # Output: -3/16

# Division
result_division = fraction1 / fraction2
print("Division:", result_division)  # Output: -4/1 (or -4)



