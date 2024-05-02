"""
Question: 200. Number of Islands
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:

    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:

    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

"""
from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visit = set()
        count = 0

        def bfs(row, col):
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            queue = collections.deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and c in range(columns) and grid[r][c] == '1' and (r, c) not in visit):
                        visit.add((r, c))
                        queue.append((r, c))
            
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visit:
                    visit.add((r, c))
                    bfs(r, c)
                    count += 1

        return count

"""
    Time-complexity = O(m*n)
    Space-complexity = O(m*n)

    Alternative solutions:
"""