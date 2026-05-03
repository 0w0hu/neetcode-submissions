class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.maxarea = 0
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r, c))

            area = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            self.maxarea = max(self.maxarea, area)
            return area

        for r in range(rows):
            for c in range(cols):
                
                if (r, c) not in visit and grid[r][c] == 1:
                    print("1111")
                    dfs(r, c)
        return self.maxarea