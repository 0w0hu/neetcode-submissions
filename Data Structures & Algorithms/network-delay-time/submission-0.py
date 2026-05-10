class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for source, target, time in times:
            adj[source].append((target,time))

        shortest = {}
        minheap = [(0, k)]
        while minheap:
            time, dest = heapq.heappop(minheap)
            if dest in shortest:
                continue
            shortest[dest] = time

            for dest2, time2 in adj[dest]:
                if dest2 not in shortest:
                    heapq.heappush(minheap, (time+time2, dest2))
        
        if len(shortest) == n:
            return max(shortest.values())
        return -1