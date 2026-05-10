class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        minheap = [(-1, start_node)]
        visit = set()

        while minheap:
            prob, cur = heapq.heappop(minheap)
            visit.add(cur)

            if cur == end_node:
                return -1 * prob

            for nei, edgeprob in adj[cur]:
                if nei not in visit:
                    heapq.heappush(minheap, (prob * edgeprob, nei))
            
        return 0