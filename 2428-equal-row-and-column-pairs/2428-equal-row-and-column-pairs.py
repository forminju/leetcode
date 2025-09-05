from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        ans = 0

        row = [tuple(r) for r in grid]
        columns = [tuple(grid[r][c] for r in range(n)) for c in range(n)]

        row_c = Counter(row)
        
        for col in columns:
            if col in row_c:
                ans += row_c[col]
        return ans

        
        