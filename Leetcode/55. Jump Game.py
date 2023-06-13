"""
I used greedy algorythm.
We iterate backward en every tyme our jump reach goal position we update our goal.
And if we reach index 0 we return True

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
