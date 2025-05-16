'''
Time O(r * c * 4^w) w = len(word)

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r,c) in path or board[r][c] != word[i]):
                return False
            if i == len(word) - 1:
                return True
            
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.pop()
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False