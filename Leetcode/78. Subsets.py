'''
Time O(n * 2^n)
Space O(n * 2^n) where n is recursive call stack
Идем по дереву сначала по левой ветке, далее мы убираем последний элемент 
и идем по другой ветке, когда сабсет заполняется добавляем его в результат
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
    