'''
ИСпользуем dfs и возвращаем в нем 2 значения: True если низжедащие
поддеревья сбалансированы а так же глубину поддерева


'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            
            balansed = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balansed, 1 + max(left[1],right[1])]
        
        return dfs(root)[0]