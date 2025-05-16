from collections import deque
'''
Recurcive DFS

Сначала описываем выход из рекурсии если у нас root будет пустым
Далее рекурсивно вызываем левую и правую ветку дерева.
Добавив max() мы можем нге волноватся что одна ветка будет короче другой

'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
'''
BFS
Используем структуру данных deque() очередь.
Если есть изначальный корень дерева джобавляем его в очередь


Далее рекурсивно вынемаем самый левый элемент в переменную node 
и смотрим есть ли у него левые и правые ветки. И добавляем уровень +1

Если есть до добавляем в очередь и так далее пока q не станет None
то есть мы достигнем конца дерева.
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q: 
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1

        return level