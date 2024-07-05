"""
Question: 875. Koko Eating Bananas

    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.

    Example 1:

    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
    Example 2:

    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
    
    Example 3:

    Input: piles = [30,11,23,4,20], h = 6
    Output: 23
"""
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
                

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res

sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))

"""
    Time-complexity = O(log(max(piles)) * O(n) = O(nlog(max(piles))
    Space-complexity = O(1)

    Alternative solutions:
    1. Brute force solution: Traverse whole search space = O(max(piles)) * O(n) = O(n^2)
"""