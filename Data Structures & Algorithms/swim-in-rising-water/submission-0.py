class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()

        minheap = [[grid[0][0], 0, 0]] #(time, r, c)
        visit.add((0, 0))
        direction = [[0,1], [0,-1], [1,0] ,[-1,0]]

        while minheap:
            t, r, c = heapq.heappop(minheap)
            visit.add((r,c))
            if r == N-1 and c == N-1:
                return t
            
            for dr, dc in direction:
                neiR, neiC = r+dr, c+dc
                if neiR not in range(N) or neiC not in range(N) or (neiR, neiC) in visit:
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minheap, [max(t, grid[neiR][neiC]), neiR, neiC])
