'''
Используем dp. Создаем массив длинной amount + 1 потому что нам нужном есто для 0
В каждый элемент записываем любое число больше amount чтобы брать потом min
И далее для каждой позиции/чимсла вычисляем сколько монет нужно для его размена
При этом блпгодоря dp[a-c] мы можем использовать результаты предидущих вычичлений. 

Time: O(a * c)
Space O(a)
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
