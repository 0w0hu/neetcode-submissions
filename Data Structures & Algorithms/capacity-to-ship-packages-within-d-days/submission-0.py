class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l+r) // 2
            time = 1
            remain = m
            for w in weights:
                if remain >= w:
                    remain -= w
                else:
                    time += 1
                    remain = m-w
            if time <= days:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res