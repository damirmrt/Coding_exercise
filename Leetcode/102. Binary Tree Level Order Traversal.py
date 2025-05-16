'''
BFS with deque


'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
 
        if root:
            q.append(root)
        
        while q:
            nodes = []
            for i in range(len(q)):
                node = q.popleft()
                nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(nodes)
        
        return res