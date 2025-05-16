'''
You are given a 
    An integer, or
    A list whose elements may also be integers or other lists.
The depth of an integer is defined by how deeply it is nested inside lists.
Your task is to return the sum of all integers in the list, weighted by their depth.

🔹 Example 2:
Input: [ [1,1], 2, [1,1] ]
Breakdown:
    First [1,1] is at depth 2 → each 1 * 2 = 2, total = 4
    2 is at depth 1 → 2 * 1 = 2
    Second [1,1] is at depth 2 → each 1 * 2 = 2, total = 4
Output: 4 + 2 + 4 = 10
'''

class NestedInteger:
    def isInteger(self) -> bool:
        return
    def getInteger(self) -> [int]:
        return
    def getList(self) -> [list['NestedInteger']]:
        return
    
import collections

class Solution:

    def depth_sum(self, nestedlist:NestedInteger):
        depth = 1
        res = 0

        queue = collections.deque(nestedlist)

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur.isInteger():
                    res += cur.getInteger() * depth
                else:
                    queue.extend(cur.getList())
                    
            depth += 1
        return res