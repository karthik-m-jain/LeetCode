"""
Question:


"""
from typing import List

class Solution:
    def maxSum(self, nums : List[int], k : int) -> int:
        
        n = len(nums)

        if( n < k ) :
            return -1
        
        window_sum = sum(nums[:k])
        array_sum = window_sum

        for i in range(n - k):
            array_sum = array_sum - nums[i] + nums[i+k]
            window_sum = max(array_sum, window_sum)

        return window_sum

solution = Solution()

print(solution.maxSum([1,4,2,10,2,3,1,0,20], 4))

"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
"""