"""
https://leetcode.com/problems/unique-paths-ii/

Same approach as in Unique Paths problem, only defference is
we set up 0 in cell if there is obstacle.

Time Complexity: O(m * n)
Space Complexity: O(n)

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        lastRow = [0] * n
        lastRow[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    lastRow[j] = 0
                elif j + 1 < n:
                    lastRow[j] = lastRow[j + 1] + lastRow[j]

        return lastRow[0]
