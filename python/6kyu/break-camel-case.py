"""
DESCRIPTION:
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    new = ""
    if s == "":
        return ""
    else:
        for ch in s:
            if ch.isupper():
                new += " " + ch
            else:
                new += ch
        return new