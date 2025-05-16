'''
Time O(n * 2^n)
Space O(n * 2^n) where n is recursive call stack

Сортируем аррэй чтобы дупликаты были рядом
Идем по дереву сначала по левой ветке, далее мы убираем последний элемент 
и идем по другой ветке но если нет дубликатов, в противном случае пропускаем его,
когда сабсет заполняется добавляем его в результат

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1,subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])

        return res