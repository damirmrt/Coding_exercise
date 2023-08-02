"""
In this solution firstly we set up zeros in first row and column
if we see zeros in array, then we fill array with zeros according first column and row

Time Complexity: O(m*n)
Space Complexity: O(1)
"""





class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # fill first row with zeros in position c if we see 0 in array on position c
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True # if zero in first row we need to fill with zeros but later

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0