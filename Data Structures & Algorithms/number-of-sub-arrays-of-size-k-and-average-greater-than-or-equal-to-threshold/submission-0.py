class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = cursum = 0
        l = 0
        for r in range(len(arr)):
            cursum += arr[r]
            if r-l+1 > k:
                cursum -= arr[l]
                l += 1
            
            if  r - l + 1 == k and cursum >= k*threshold:
                count += 1
            
        return count
            
