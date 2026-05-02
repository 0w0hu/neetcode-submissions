class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        
        for t in tasks:
            count[t] = count.get(t, 0) - 1
        print(count)
        maxheap = list(count.values())
        heapq.heapify(maxheap)

        time = 0
        q = deque() #[-cnt, idletime]

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt != 0:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(maxheap, cnt)
        return time
