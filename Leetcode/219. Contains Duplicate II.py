'''
Given an integer array nums and an integer k, return true if there
are two distinct indices i and j in the array such that nums[i] == nums[j]
and abs(i - j) <= k.

 
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i = 0 
        res = set()
        for j in range(len(nums)):
            if j - i > k:
                res.remove(nums[i])
                i += 1
            if nums[j] in res:
                return True
            res.add(nums[j])
        return False
    
nums = [1,2,3,1]
k = 3

l = Solution()
print(l.containsNearbyDuplicate(nums, k))