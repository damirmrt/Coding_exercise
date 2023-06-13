"""
Similar to Jump Game 1 I used Greedy algorythm, but in this solution
I iterate from begining.

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        counter = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):  # iteration in window defined by maximum jump
                farthest = max(farthest, i + nums[i])  # maximise our jump
            l = r+1
            r = farthest
            counter += 1

        return counter
