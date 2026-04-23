class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = 0
        count = 0
        for n in nums:
            if count == 0:
                maj = n
            count += (1 if n == maj else -1)
        return maj
