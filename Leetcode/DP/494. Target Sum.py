'''
dfs на каждом шаге мы рекурсивно добавляем и вычитаем число.
Для треккинга общей суммы добавляем переменную target
'''

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i >= len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[(i, total)]
        
        return dfs(0, 0)