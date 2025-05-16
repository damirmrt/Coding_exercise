'''
DP O(1) memory

Используется последовательность фибонначи, мы добавляем два предидущих числа 
потому что для них мы уже вычислили сколько уникальных способов добраться до конца есть
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        n1 = 1
        n2 = 2

        for i in range(n - 2):
            tmp = n2
            n2 = n1 + n2
            n1 = tmp

        return n2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]