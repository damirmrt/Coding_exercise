'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7
'''

'''

'''

class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        cur = prev = res = 0
        cur_operation = '+'

        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if cur_operation == '+':
                    res += cur
                    prev = cur
                elif cur_operation == '-':
                    res -= cur
                    prev = -cur
                elif cur_operation == '*':
                    res -= prev
                    res += prev * cur

                    prev = cur * prev
                else:
                    res -= prev
                    res += int(prev / cur)

                    prev = int(prev / cur)
                cur = 0
            elif cur_char != ' ':
                cur_operation = cur_char
            i += 1
        
        return res