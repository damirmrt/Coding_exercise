"""
Simple two pointers solution

# This is very easy problem, have no clue why it is marked as medium

Time Complexity: O(n)
Space Complexity: O(n) # due to the join function

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        l, r = 0, len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ' '.join(s)
    