class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            # [3,4,5,1,2]

            # we need to confirm which part we landed,
            # one case is that we landed on the left portion, 
            # which means that nums[m] > nums[l]
            if nums[m] >= nums[l]:
                # now we need to check the target,
                # if target > nums[m] or target < nums[l], 
                if target > nums[m] or target < nums[l]:
                    # then we need to search on the right 
                    l = m + 1
                else:
                    # other wise search on left
                    r = m - 1

            # another case is that we landed on the right portion,
            # which means that nums[m] < nums[r]
            else:
                # now we need to check the target,
                # if target > nums[r] or target < nums[m], 
                if target > nums[r] or target < nums[m]:
                    # then we need to search on the left
                    r = m - 1
                else:
                    l = m + 1
                
        return -1