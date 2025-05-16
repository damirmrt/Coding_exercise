'''
счоздаем матрицу и с помощью DP идем по ней в обратном направлении

	c	a	t	
c	2	2	1	0
a	2	2	1	0
r	1	1	1	0
b	1	1	1	0
t	1	1	1	0
	0	0	0	0

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] =  1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]