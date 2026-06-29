class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            heapq.heappush(stones, -1*abs(x-y))
        
        return -1 * stones[0] if stones else 0