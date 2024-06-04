"""
Question: 46. Permutations

    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]

"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in nums:
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)

        return result
    
solution = Solution()
print(solution.permute([1,2,3]))

"""
    Time-complexity = O(n*2^n)
    Space-complexity = O(n*2^n)

    Alternative solutions:
"""