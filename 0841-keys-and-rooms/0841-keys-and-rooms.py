class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        stack = [0]
        visited[0] = True

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    stack.append(key)
                    visited[key] = True

        return all(visited)
        