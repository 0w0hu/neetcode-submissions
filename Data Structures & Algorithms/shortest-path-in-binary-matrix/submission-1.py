class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        q.append((0, 0))
        visit = set()
        neighbour = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ]
        path = 1

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows-1 and c == cols-1:
                    return path
                
                for dr, dc in neighbour:
                    row, col = r+dr, c+dc
                    if row not in range(rows) or col not in range(cols) or (row, col) in visit or grid[row][col] == 1:
                        continue
                    visit.add((row, col))
                    q.append((row, col))
            path += 1
                
        return -1
            