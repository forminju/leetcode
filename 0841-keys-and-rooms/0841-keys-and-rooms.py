from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        
        while q :
            room = q.popleft()

            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    q.append(key)

        return all(visited)

        