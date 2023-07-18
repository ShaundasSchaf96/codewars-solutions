"""
DESCRIPTION:
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""


def maps(a):
    new = []
    for num in a:
        num = num * 2
        new.append(num)
    return new
