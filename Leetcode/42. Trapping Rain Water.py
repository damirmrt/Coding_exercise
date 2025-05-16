'''
Time Complexity: O(n*m) n = len(height) m = max(height)
Space Complexity: O(1)
'''
class Solution:
    def trap(self, height: list[int]) -> int:
        counter = 0
        for h in range(max(height)):
                l = 0
                r = len(height) - 1
                while height[l] - h <= 0 or height[r] - h <= 0:
                    if height[l] - h <= 0:
                        l += 1
                    elif height[r] - h <= 0: 
                        r -= 1
                    elif l >= r:
                        break
                for i in range(l, r + 1, 1):
                    if height[i] - h <= 0:
                        counter += 1
        return counter
'''
Time Complexity: O(n) n = len(height)
Space Complexity: O(1)
'''
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
