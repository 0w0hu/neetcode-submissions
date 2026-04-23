class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        num = sorted(nums)
        res = []
        for i, n in enumerate(num):
            if n > 0:
                break
            if i > 0 and n == num[i - 1]:
                continue
            l = i+1
            r = len(num) - 1
            while l < r:
                threeSum = n + num[l] + num[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, num[l], num[r]])
                    l += 1
                    r -= 1
                    while num[l] == num[l - 1] and l < r:
                        l += 1

        return res
        
