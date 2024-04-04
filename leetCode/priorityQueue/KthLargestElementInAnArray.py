"""
Question: 215. Kth Largest Element in an Array
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?

    Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
"""
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return -heapq.heappop(nums)

sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

"""
    Time-complexity = O(klogn + n)
    Space-complexity = O(1)

    Alternative solutions:
"""