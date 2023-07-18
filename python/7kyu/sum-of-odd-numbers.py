"""
DESCRIPTION:
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


def row_sum_odd_numbers(n):
    sum = 0
    start = (n*n) - (n-1)
    end = start + (n*2)
    for i in range(start, end, 2):
        sum += i
    return sum