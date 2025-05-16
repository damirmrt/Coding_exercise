'''
recurcive dfs

мы будем записывать в результат 1 если нода больше чем макс значение
и там сделаем для каждой ноды
res += позволит накаппливать количество нод
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0
            res = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)
            res += dfs(root.left,max_val)
            res += dfs(root.right,max_val)

            return res
        return dfs(root,root.val)