"""
Question: 150. Evaluate Reverse Polish Notation

    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    

    Example 1:

    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    Example 2:

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
    Example 3:

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    

    Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if i == '+':
                    stack.append(operand1 + operand2)
                elif i == '-':
                    stack.append(operand1 - operand2) 
                if i == '*':
                    stack.append(operand1 * operand2) 
                if i == '/':
                    # when you divide two integers using the / operator, the result is a floating-point number, even if the division could result in an integer
                    # the int() truncates the decimal value
                    stack.append(int(operand1 / operand2))

        return stack.pop()  
        
solution = Solution()

print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


"""
    Time-complexity = O(n)
    Space-complexity = O(n)

    Alternative solutions:
"""