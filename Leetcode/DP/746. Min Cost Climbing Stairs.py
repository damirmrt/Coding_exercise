'''
Идем с конца в начало. И складываем минимум двух предидущих значений
с текущим. Аналогично с задачей Climbing stairs
'''

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost) -3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])

