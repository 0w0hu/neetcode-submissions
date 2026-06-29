class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r not in range(row) or c not in range(col) or (r,c) in visit or grid[r][c] == "0":
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        island = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visit and grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        return island