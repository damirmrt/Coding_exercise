'''
s = "AABABBA", k = 1
Создаем словарь и с помощью sliding window заносим в него буквы и их количество,
далее считаем самые частые буквы и смотри сколько менее частых которые мы должны заменить
если их не больше чем к обновляем результат, если больше, двигаем левый указатель
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowMap = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)
            

            while (r - l + 1) - max(windowMap.values()) > k:
                windowMap[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len