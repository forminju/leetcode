class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        answer = 0

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        def dfs(x,y):
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx <n and 0<= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == '1':
                        dfs(nx,ny)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    answer +=1
                    dfs(i,j)

        return answer



            


        