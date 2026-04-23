class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for n in nums:
            if n in viewed:
                return True
            viewed.add(n)
        return False