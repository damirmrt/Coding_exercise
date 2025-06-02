'''

'''

class Solution:
    def minKnightMoves(self, x: int, y: int):
         
        x, y = abs(x), abs(y)

        steps = [(2, -1), (1, -2), (-1, -2), (-2, -1), 
                (-1, 2), (1, 2), (2, 1), (-2, 1)]

        visited = set()

        q = [(0, [0, 0])]

        while q:
            moves, coords = q.pop(0)
            if coords[0] == x and coords[1] == y:
                return moves
            
            for s in steps:
                next = (coords[0] + s[0], coords[1] + s[1])

                if ((next[0], next[1]) not in visited and
                    next[0] >= -1 and next[1] >= -1):
                    visited.add((next[0], next[1]))
                    q.append((moves + 1,[next[0], next[1]]))

        return -1
                
s = Solution()
x = -1
y = -0
print(s.minKnightMoves(x,y))

                   
              