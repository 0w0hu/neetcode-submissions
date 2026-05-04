class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        land = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    land += 1
                if grid[r][c] == 0:
                    q.append((r, c))
        
        step = 1
        while q or land > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 2147483647:
                        continue
                    grid[r][c] = step
                    q.append((r,c))
                    land -= 1
            step += 1


        



        
        