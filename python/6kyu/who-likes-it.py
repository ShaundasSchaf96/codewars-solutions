"""
DESCRIPTION:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""


def likes(names):
    names_list = list(names)
    if len(names_list) == 0:
        return "no one likes this"
    elif len(names_list) == 2:
        return names_list[0] + " and " + names_list[1] + " like this"
    elif len(names_list) == 3:
        return names_list[0] + ", " + names_list[1] + " and " + names_list[2] + " like this"
    elif len(names_list) == 1:
        return names_list[0] + " likes this"
    else:
        return ', '.join(names_list[0:2]) + f" and {len(names_list) - 2} others like this"
