class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = [False] * n

        def dfs(prov):
            visited[prov] = True

            for nxt in range(n):
                if isConnected[prov][nxt] == 1 and visited[nxt] == False:
                    dfs(nxt)

        
        ans = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans+=1

        return ans
                

        