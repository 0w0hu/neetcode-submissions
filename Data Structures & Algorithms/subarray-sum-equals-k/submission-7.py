class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        cursum = 0
        res = 0
        
        for n in nums:
            cursum += n
            diff = cursum - k
            res += hashmap.get(diff, 0)
            hashmap[cursum] = 1 + hashmap.get(cursum, 0)
        return res