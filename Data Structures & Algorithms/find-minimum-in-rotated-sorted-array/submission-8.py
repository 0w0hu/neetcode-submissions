class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            # now we need to think about the update method
            # one condition is that we landed on the left portion:
            # which means that our nums[m] > nums[l] and nums[m] < nums[r], 
            # in this case the smaller integer will be on the right side
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            # another condition is that we landed on the right portion:
            # which means that our nums
            else:
                r = m - 1
            
        return res
        

            
            
            