class Solution:
    def maxArea(self,
                height: list[int]) -> int:
        # This is two pointers approach you start from the opposite sides of array and calculate Q for each step
        l,r = 0, len(height)-1
        max_Q = 0

        while l < r:
            q = min(height[l],height[r])*(r-l)
            if max_Q < q:
                max_Q = q  # rewrite max_Q if it's bigger than previous
            if height[l]<height[r]:  # move pointer that lower in order to maximize Q
                l += 1
            else:
                r -= 1

        return max_Q