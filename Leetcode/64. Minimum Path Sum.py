class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        res = [[float('inf')] * (cols + 1) for row in range(rows + 1)]
        # initialize new grid which bigger than initial by 1 for each side
        res[rows - 1][cols] = 0  # initialize 0 below grid[-1][-1] for initial min() choice

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])

        return res[0][0]
