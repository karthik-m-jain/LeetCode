# Two pointers technique

from typing import List

def isPairSum(nums: List[int], target: int) -> bool:
    i = 0
    j = len(nums)-1
    while(i<j):
        if(nums[i] + nums[j]) == target:
            return True
        elif (nums[i]+nums[j]) < target:
            i += 1
        else:
            j -= 1
    return False

print(isPairSum([2,3,5,8,9,10,11], 17))