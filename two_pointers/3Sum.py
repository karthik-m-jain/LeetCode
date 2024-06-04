"""
Question:
    15. 3Sum
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()     #in-place sort
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:    #to check if neighboring value is same or not and prevent duplicates
                continue
            else:
                j, k = i+1, len(nums)-1     #two sum II
                while(j<k):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while nums[j] == nums[j-1] and j<k:     #to prevent same values at different j and k are not inserted in the list
                            j += 1
                    elif(nums[i] + nums[j] + nums[k] > 0):
                        k -= 1
                    else:
                        j += 1
        return result
    
solution = Solution()

print(solution.threeSum([-1,0,1,2,-1,-4]))

"""
    Time-complexity = O(n^2) + O(nlogn) [For sorting] -> O(n^2)
    Space-complexity = O(1) as we used sort() which in-place sorting. If sorted() was used that creates new list then O(n)

    Alternative solutions:
    1. Create a 3-level for loop and traverse each combination and check for duplicates before inserting the combination
"""