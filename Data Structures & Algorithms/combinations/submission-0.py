class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        cur = []

        def helper(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                cur.append(j)
                helper(j+1, cur)
                cur.pop()
        helper(1, cur)
        return res