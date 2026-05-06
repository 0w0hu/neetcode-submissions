class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        s1, s2 = cost[-2], cost[-1]
        for i in range(len(cost)-3,-1,-1):
            tmp = s1
            s1 = cost[i] + min(s1, s2)
            s2 = tmp
        return min(s1, s2)