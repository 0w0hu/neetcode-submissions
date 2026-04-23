class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l < r:
            intSum = numbers[l] + numbers[r] 
            if intSum < target:
                l += 1
            elif intSum > target:
                r -= 1
            else:
                return [l+1, r+1]