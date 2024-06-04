"""
Question: 695. Max Area of Island

    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
    The area of an island is the number of cells with a value 1 in the island.
    Return the maximum area of an island in grid. If there is no island, return 0.

    Example 1:

    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

    Example 2:

    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0
"""
from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visit = set()
        area = 0

        def bfs(row, col):
            directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
            queue = collections.deque()
            count = 1
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    i, j = r + dr, c + dc
                    if (i in range(rows) and j in range(columns) and grid[i][j] == 1 and (i, j) not in visit):
                        visit.add((i, j))
                        queue.append((i, j))
                        count += 1

            return count

        for r in range(rows):
            for c in range(columns):
                if(grid[r][c] == 1 and (r,c) not in visit):
                    visit.add((r,c))
                    area = max(area, bfs(r, c))

        return area

"""
    Time-complexity = O(m*n)
    Space-complexity = O(m*n)

    Alternative solutions:
"""