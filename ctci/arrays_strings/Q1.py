"""
Question: Is Unique
    Implement an algorithm to determine if a string has all unique characters.
"""

def isUnique(name):
    # String of unique characters cannot extend 128 characters
    if len(name) > 128:
        return False
    
    #Set because of the unique property of no duplicates
    character_array = set()

    for i in name:
        if i in character_array:
            return False
        character_array.add(i)

    return True

print(isUnique("KarthiK"))

"""
    Time-complexity = O(n) precisely it is O(c) where C is the length of character set
    Space-complexity = O(n) as we create a new set of size 'n'

    Alternative solutions:
    1. Check each character with every other character = O(n^2)
    2. Sort and check the alternate characters = O(nlogn)
"""