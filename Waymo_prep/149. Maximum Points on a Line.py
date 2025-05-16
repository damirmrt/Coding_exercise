'''
Итерируемся по каждой точке, далее инициализируем словарь в который 
будем записывать склон каждой прямой на которую эти точки ложатиься
Time O(n^2)
Space O(n)
'''

import collections
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i+1,len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1])/(p2[0] - p1[0])
                    count[slope] += 1
                    res = max(res, count[slope] + 1)
        return res