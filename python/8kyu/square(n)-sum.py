"""
DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9.
"""


def square_sum(numbers):
    sum = 0
    for number in numbers:
        number = number**2
        sum += number
    return sum