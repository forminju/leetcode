class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        
        visited = [False] * n


        def dfs(room:int):
            visited[room] = True
            for key in rooms[room]:
                if visited[key] == False:
                    dfs(key)

        
        dfs(0)

        return all(visited)








        