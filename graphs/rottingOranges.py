"""
Question: 994. Rotting Oranges

    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    Example 1:

    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Example 2:

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    Example 3:

    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.    
"""
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()
        fresh, time = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        while queue and fresh > 0:
            for q in range(len(queue)):
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1],[0, -1]]

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append([r, c])

            time += 1

        return time if fresh == 0 else -1
  
"""
    Time-complexity = 
    Space-complexity = 

    Alternative solutions:
"""