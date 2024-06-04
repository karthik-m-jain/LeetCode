"""
Question:
    167. Two sums II - Input Array is sorted
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space. 

    Example 1:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while(i < j):
            if (numbers[i] + numbers[j] == target):
                return [i+1, j+1]
            elif (numbers[i] + numbers[j] >target):
                j -= 1
            else:
                i += 1

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))

"""
    Time-complexity = O(nlogn) - due to sorting
    Space-complexity = O(1)

    Alternative solutions:
    1. Brute force - Use first for loop and compare all the other elements using another loop
"""