'''
https://leetcode.com/problems/unique-paths/

This solution is using Dynamic Programming approach.
We go from bottom right, row by row, in each cell we add right cell and bottom cell.
In the end we just return index 0 of our last row

Time Complexity: O(m * n)
Space Complexity: O(n)

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * n  # initialize last row with ones

        for i in range(m-1):
            row = [1] * n
            for j in range(n-2, -1, -1):  # n-2 in order not to go out of bounds
                row[j] = row[j+1] + lastRow[j]
            lastRow = row

        return lastRow[0]