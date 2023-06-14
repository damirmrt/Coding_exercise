'''
This solution uses simple 1D Dynamic Programing approach

    [3]      dp = [23, 19, 15, 3, 0]
   [7, 4],   dp = [20, 19, 15, 3, 0]
  [2, 4, 6]  dp = [10, 13, 15, 3, 0]
[8, 5, 9, 3] dp = [8, 5, 9, 3, 0]
             dp = [0, 0, 0, 0, 0]

Time Complexity: O(n * m)
Space Complexity: O(n)
'''

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i+1])

        return dp[0]