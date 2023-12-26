"""
217. Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: true

    Example 2:

    Input: nums = [1,2,3,4]
    Output: false

"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Set because of the unique property of no duplicates
        exists_array = set()
        for i in nums:
            if i in exists_array:
                return True
            exists_array.add(i)
        return False
    
# Create an instance of the Solution class
solution_instance = Solution()

# Test the containsDuplicate method with a list of integers
test_nums1 = [1, 2, 3, 4, 5]
test_nums2 = [1, 2, 3, 1, 4, 5]

result1 = solution_instance.containsDuplicate(test_nums1)
print(result1)

result2 = solution_instance.containsDuplicate(test_nums2)
print(result2)

"""
    Time-complexity = O(n)
    Space-complexity = O(n) as we create a new set of size 'n'

    Alternative solutions:
    1. Check each integer with every other integer = O(n^2)
    2. Sort and check the alternate integer = O(nlogn)
"""