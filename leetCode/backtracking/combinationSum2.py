"""
Question: 40. Combination Sum II

    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.

    Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

    Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return 

            curr.append(candidates[i])
            backtrack(i+1, curr, total + candidates[i])
            curr.pop()

            while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1
                
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return result
        
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))

"""
    Time-complexity = O(k*2^n) -> time to copy + combinations
    Space-complexity = 

    Alternative solutions:
"""