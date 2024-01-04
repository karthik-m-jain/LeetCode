"""
Question: Check permutation
    Given two strings, write a method to decide if one is a permutation of the other

Assumption: Case-sensitive and whitespace is significant 
"""

def isPermutation(s1, s2):
    #if length of two strings is unequal
    if len(s1)!=len(s2):
        return False
    
    #dictionary (char:count)
    char_dict = {}

    for i in s1:
        char_dict[i] = char_dict.get(i, 0) + 1
    
    for i in s2:
        char_dict[i] = char_dict.get(i, 0) - 1
        if(char_dict[i] < 0):
            return False
    return True

    #solution 2 = O(logn)
    # if sorted(s1) == sorted(s2):
    #     return True
    # return False

print(isPermutation("God", "ogd"))

"""
    Time-complexity = O(n)
    Space-complexity = O(n)

    Alternative solutions:
    1. Arrange each character of string in ascending order = O(nlogn)
"""