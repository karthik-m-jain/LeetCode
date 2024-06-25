"""
Question: 22. Generate Parentheses

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    
    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    
    Example 2:
    Input: n = 1
    Output: ["()"]
    
    Constraints:
    1 <= n <= 8

"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    
sol = Solution()
print(sol.generateParenthesis(1))

"""
    Time-complexity = O(2*n)
    Space-complexity = O(n)

    Alternative:

"""