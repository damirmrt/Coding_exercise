'''
DFS

Time O(m*n)
Space O(m*n)
'''

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (min(r, c) < 0 
                or r >= rows 
                or c >= cols 
                or (r, c) in visit
                or grid[r][c] == '0'
            ):
                return
            visit.add((r, c))
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r - 1,c)
            dfs(r,c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)

        return islands
        