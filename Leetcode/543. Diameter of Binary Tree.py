'''
DFS approach

для каждого корня дерева мы рекурсивно вычисляем глубину левой и правой части
и добавляем их сумму в res
При этом return этой функции возвращает рукурсивно накопленную глубину 

nonlocal res - нужно чтобы переменная считалась в функции
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return res