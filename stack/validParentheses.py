"""
Question: 
    20. Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
    
    Example 1:

    Input: s = "()"
    Output: true

    Example 2:

    Input: s = "()[]{}"
    Output: true
    
    Example 3:

    Input: s = "(]"
    Output: false
"""

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        sequence_map = {')': '(', '}':'{', ']':'['}

        for i in s:
            if i in sequence_map:
                if stack and stack[-1] == sequence_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        if not stack:
            return True
        else:
            return False

solution = Solution()

print(solution.isValid('(){}'))

"""
    Time-complexity = O(n)
    Space-complexity = O(n)

    Alternative solutions:
    1. Use if-else instead of Hash-map
"""