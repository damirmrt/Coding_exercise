"""

In this solution I used 4 pointers approach. I iterate over all numbers in outer rows,
then increment pointers by one till they met each other

Time Complexity: O(n*m)
Space Complexity: O(1)

"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                topleft = matrix[top][l + i]  # store first value to the final rotation

                # Rotate in reverse order

                matrix[top][l+i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top+i][r]
                matrix[top + i][r] = topleft

            r -= 1
            l += 1
