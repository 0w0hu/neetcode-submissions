class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            subarr = 1
            cursum = 0
            for n in nums:
                cursum += n
                if cursum > largest:
                    subarr += 1
                    cursum = n
            return subarr <= k
        
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l+r) // 2
            if cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res