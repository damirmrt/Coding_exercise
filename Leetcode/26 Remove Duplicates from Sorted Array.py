"""
# input nums =  [0,0,1,1,1,2,2,3,3,4]
# output nums = [0,1,2,3,4,2,2,3,3,4]
                    #    ^ variable duplicate moove all non-dulicated values till here
                    #   rest of the array is just copy of previous
                    #   you can print array without duplicates by nums[:len(nums)-duplicates]

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        duplicates = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # compare two values
                duplicates += 1
            else:  # if duplicate sequence is over we move our value to the position of first duplicate
                nums[i - duplicates] = nums[i]

        return len(nums) - duplicates



