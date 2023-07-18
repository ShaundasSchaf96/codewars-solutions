"""
DESCRIPTION:
Your function takes two arguments:

1. current father's age (years)
2. current age of his son (years)

Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
"""


def twice_as_old(dad_years_old, son_years_old):
    age_twice_as_old = 2 * son_years_old
    difference = dad_years_old - age_twice_as_old
    return abs(difference)