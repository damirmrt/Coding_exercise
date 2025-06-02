'''
BFS.
Visited is matrix with accumulation values
'''
from collections import deque

class Solution:
    def shortestDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        dist_matrix = [[0] * cols for row in  range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        min_dist = float('inf')
        empty_land = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    local_dist = float('inf')

                    queue = deque([(row, col, 0)])

                    while queue:
                        cur_row, cur_col, distance = queue.popleft()

                        for row_inc, col_inc in directions:
                            new_row = row_inc + cur_row
                            new_col = col_inc + cur_col

                            if ((0 <= new_row < rows) and (0 <= new_col < cols)
                                and grid[new_row][new_col] == empty_land):
                                grid[new_row][new_col] -= 1
                                dist_matrix[new_row][new_col] = distance + 1

                                queue.append((new_row, new_col, distance + 1))

                                local_dist = min(local_dist, dist_matrix[new_row][new_col])

                    empty_land -= 1
                    min_dist = local_dist

        return min_dist if min_dist != float('inf') else -1    
