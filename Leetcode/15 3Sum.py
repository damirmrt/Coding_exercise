
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # iterate over first element of our three sums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            # iterate over rest two element of our three sums
            while l < r:
                threeSumm = nums[i] + nums[l] + nums[r]
                # We just move our left pointer if sum > target or move right pointer if sum < target
                if threeSumm > 0:
                    r -= 1
                elif threeSumm < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
