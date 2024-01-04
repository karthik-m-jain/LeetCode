"""
Question: URLify
    Replace space in the string with "%20"

Tip: 
    1. Try to achieve in-place update
    2. Strings in Python are immutable so create a list of characters of string
"""

def replaceString(string, length):

    temp_index = len(string)
    print(temp_index)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[temp_index - 3 : temp_index] = '%20'
            temp_index -= 3
        else:
            string[temp_index-1] = string[i]
            temp_index -= 1

    return string

print(replaceString(list('Mr John Smith    '), 13))

"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
    1. Create a new array and traverse the original array along with manipulating the new array
"""