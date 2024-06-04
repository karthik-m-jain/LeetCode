"""
Question:
    11. Container with most water
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 1, len(height)
        result = 0

        while(l<r):
            area = min(height[l-1], height[r-1]) * (r-l)
            result = max(result, area)

            if(height[l-1]<height[r-1]):
                l += 1
            else:
                r -= 1

        return result

solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

"""
    Time-complexity = O(n)
    Space-complexity = O(!)

    Alternative solutions:
    1. Brute force - Use two loops can calculate every combination = O(n^2)
"""