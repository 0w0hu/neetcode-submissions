class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq)-1,-1,-1):
            for c in freq[i]:
                ans.append(c)
                if len(ans) == k:
                    return ans