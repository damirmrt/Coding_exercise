'''
содаем список длиной s + 1 для того чтобы в послднюю фиктивную ноду поместить True 
Это нужно для того чтобы первое совпадение сработало
Далее итерируемся в обратном порядки и для каждного i проверяем каждое слово.
Проверка идет взятием True с предидущего совпадения. 
'''

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s)-1 , -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]