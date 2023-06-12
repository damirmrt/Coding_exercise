"""
https://leetcode.com/problems/unique-paths-iii

In this solution I used DFS and backtracking

"""

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start_r, start_c, end_r, end_c = 0, 0, 0, 0

        empty = 0
        # Firstly we need to define starting position, end position and
        # number of empty lines, because we need to step on every line to reach condition
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 2:
                    end_r, end_c = r, c
                elif grid[r][c] == 0:
                    empty += 1

        self.output = 0
        visited = set()

        def dfs(r, c, visited, walk):
            if r == end_r and c == end_c:  # if we reach end
                if walk == empty + 1:  # and if we go through every empty cell
                    self.output += 1
                return

            if 0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r, c) not in visited:
                visited.add((r, c))
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(r + i, c + j, visited, walk + 1)  # recursive call
                visited.remove((r, c))

        dfs(start_r, start_c, visited, 0)

        return self.output
