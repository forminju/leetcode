class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        answer = []
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        def dfs(x,y):
            visited[x][y] = True
            area = 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == False and grid[nx][ny] == 1 :
                        area += dfs(nx,ny)
            
            return area

        max_area = 0

        
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == 1 :

                    max_area = max(max_area, dfs(i,j))

        
        return max_area


        