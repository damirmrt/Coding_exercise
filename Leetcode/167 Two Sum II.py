"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self,
               numbers: list[int],
               target: int) -> list[int]:
        l = 0
        r = len(numbers)-1

        # We know that our input array is sorted!
        # We just move our left pointer if sum > target or move right pointer if sum < target

        while r > l:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return [l+1,r+1]