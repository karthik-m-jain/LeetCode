"""
Question: 739. Daily Temperatures

    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    
    Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    
    Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair = [value, index]
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                tmp, index = stack.pop()
                res[index] = i - index
            stack.append([temperatures[i], i])   
        return res

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

"""
    Time-complexity = O(n)
    Space-complexity = O(n)

    Alternative solutions:
    1. Brute force - Check all elements ahead and compare = O(n^2)
"""