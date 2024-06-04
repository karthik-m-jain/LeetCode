"""
Question: 

    1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
       You may assume that each input would have exactly one solution, and you may not use the same element twice.
       You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Solution 1 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        #Solution 2
        visited = {}
        for i in range(len(nums)):
            if (target - nums[i]) in visited:
                return [visited[target-nums[i]],i]
            else:
                visited[nums[i]] = i

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))

"""
    Solution 2
    Time-complexity = O(n)
    Space-complexity = O(n)

    Solution 1
    Time-complexity = O(n^2)
    Space-complexity = O(1)
"""

