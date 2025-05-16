from collections import defaultdict

n = 4, dislikes = [[1,2],[1,3],[2,4]]

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        # create dict with keys as person and value a list of all disliked person

        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c  
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - c): # 1-c check adjacent nodes
                    return False
            return True

        for person in range(1, n + 1):
            if person not in color:
                if not dfs(person, 0):
                    return False

        return True
    

