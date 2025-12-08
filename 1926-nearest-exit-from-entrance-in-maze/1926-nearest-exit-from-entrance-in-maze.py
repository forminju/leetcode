from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        er, ec = entrance
        visited[er][ec] = True

        q = deque()
        q.append((er,ec,0))

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        while q:
            # 먼저 뽑는 거 부터 해야지!!
            x, y, dist = q.popleft()

            if (x==0 or x == m-1 or y == 0 or y == n-1) and [x,y]!=entrance:
                return dist

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<m and 0<=ny<n and maze[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1))

        return -1



        