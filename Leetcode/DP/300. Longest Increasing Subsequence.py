'''
Time O(n^2)

И дем  по списку обратно и во втором цикле сравниваем число со всеми
следующими цифрами в прямом порядке. Если число больше то добавляем eдиницу 
и значение накопленной последовательности для следующегогь числа
'''

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
