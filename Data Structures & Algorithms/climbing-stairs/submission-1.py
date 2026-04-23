class Solution:
    def climbStairs(self, n: int) -> int:

        curr, prev = 1, 0

        for i in range(n):
            tmp = curr
            curr = curr + prev
            prev = tmp
        
        return curr


            