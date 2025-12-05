from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            changes = 0
            for nei, cost in graph[node]:
                if not visited[nei]:
                    changes +=cost
                    changes +=dfs(nei)
            return changes

        return dfs(0)
        