
class Solution:
    def twoSum(self,
               nums: list[int],
               target: int) -> list[int]:

        d = {}
        for index, value in enumerate(nums):
            r = target - value
            if r in d:  # check if second value in d
                return [d[r], index]
            d[value] = index # add value to d


