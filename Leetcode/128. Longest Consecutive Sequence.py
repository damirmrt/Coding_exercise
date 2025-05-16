'''
Создаем сет чтобы избавится от дупликатов. Поиск в сете совершавется за О(1).
Для каждого числа в сете смотрим есть ли число меньше его, если нет, то это начало
последовательности. Заходим в цикл while смотрим есть ли в сете числа больше текущего на один,
если есть добавляем к длине 1. ЕПсли последовательность заканчивается,берем максимум
для нахождения самой длинной.
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                lenght = 1
                while (n + lenght) in nums_set:
                    lenght += 1
                longest = max(lenght, longest)
            
        return longest
