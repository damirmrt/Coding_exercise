'''
нам нужно псчитать cur_max и cur_min потому что два числа могут быть отрицательные 
тогда при умножении мы можем получить новое боольшое положимтельное число.
'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = 1
        cur_min = 1
        res = nums[0]

        for n in nums:
            tmp = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp, cur_min * n, n)

            res = max(res, cur_max)
        return res