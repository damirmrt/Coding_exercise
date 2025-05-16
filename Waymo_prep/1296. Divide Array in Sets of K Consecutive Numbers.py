'''
считаем количество каждого значения и далее с помощью кучи 

O(nlogn)
O(n)
'''
import heapq

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k:
            return False

        count = {}

        for n in nums:
            count = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
