class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(node):
            visited[node] = True
            for nei in range(n):
                if not visited[nei] and isConnected[nei][node] ==1:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                provinces +=1
                dfs(i)

        return provinces
        