class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for _ in range(n)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        def dfs(x,y):
            visited[x][y] = True
            is_closed = True

            if x == 0 or x == n-1 or y == 0 or y ==m-1:
                is_closed = False
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == False and grid[nx][ny] ==0:
                        if not dfs(nx,ny):
                            is_closed = False

            return is_closed

        answer = 0
        for i in range(n-1):
            for j in range(m-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    if dfs(i,j):
                        answer +=1

        return answer
                


        