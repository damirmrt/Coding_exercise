'''
Итерируемся сначала по рядам, сравнивая с таргетом краевые значения ряда
если таргет внут ри ряда, разрываем цикл
и потом осуществляем бинарный поиск в ряде. 
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
                
        top, bot = 0, rows - 1
        while top <= bot:
            m = (bot + top) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, cols - 1
        m = (bot + top) // 2
        while l <= r:
            n = (r + l) // 2
            if target > matrix[m][n]:
                l = n + 1
            elif target < matrix[m][n]:
                r = n - 1
            else:
                return True
        return False
    
