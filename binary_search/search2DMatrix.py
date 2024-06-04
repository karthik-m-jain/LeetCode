"""
Question: 74. Search a 2D Matrix
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
    target = 3
    Output: true

    Example 2: 
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
    target = 13
    Output: false

    Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while (top <= bottom):
            middle = (top + bottom)//2
            if(matrix[middle][right] < target):
                top = middle + 1
            elif(matrix[middle][0] > target):
                bottom = middle - 1
            else:
                res = middle
                break
        
        if top>bottom:
            return False
                
        while (left <= right):
            m = (left + right)//2
            if (matrix[res][m] < target):
                left = m + 1
            elif (matrix[res][m] > target):
                right = m - 1
            else:
                if(matrix[res][m] == target):
                    return True
        
        return False

solution = Solution()

print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


"""
    Time-complexity = O(log(m*n))
    Space-complexity = O(1)

    Alternative solutions:
"""