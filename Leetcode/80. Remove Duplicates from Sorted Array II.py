"""
Two pointer solution, we move right pointer till number change
than we iterate over min(2,counter) because we need left 2 same numbers or less.
In other words each time we move left pointer maximum by 2 positions, and overwrite rest.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            counter = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                counter += 1

            for i in range(min(2, counter)):
                nums[l] = nums[r]
                l += 1
            r += 1

        return l