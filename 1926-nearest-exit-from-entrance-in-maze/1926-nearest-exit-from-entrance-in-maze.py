from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        er,ec = entrance
        visited = [[False]*n for _ in range(m)]
        visited[er][ec] = True

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        q = deque()
        q.append((er,ec,0))

        while q:
            x,y,dist = q.popleft()
            if (x==0 or x==m-1 or y == 0 or y == n-1) and [x,y]!=entrance:
                return dist

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<m and 0<=ny<n and maze[nx][ny] =='.' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1))

        return -1
        