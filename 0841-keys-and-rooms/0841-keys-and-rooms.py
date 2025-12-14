from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        q = deque([0])

        while q:
            room = q.popleft()
            for key in rooms[room]:
                if visited[key] == False:
                    visited[key] = True
                    q.append(key)

        return all(visited)




        