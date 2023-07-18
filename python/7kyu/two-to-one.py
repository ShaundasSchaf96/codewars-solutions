"""
DESCRIPTION:
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


def longest(a1, a2):
    a3 = ""
    for letter in a1:
        if letter not in a3:
            a3 += letter
            for ch in a2:
                if ch not in a3:
                    a3 += ch
    return "".join(sorted(a3))