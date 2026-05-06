class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        cache = {}
        def dfs(l, r):
            if 0 > l or r == len(s):
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            if s[l] == s[r]:
                length = 1 if l == r else 2
                cache[(l, r)] = length + dfs(l-1, r+1)
            else:
                cache[(l, r)] = max(dfs(l-1, r), dfs(l, r+1))
            return cache[(l, r)]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i+1)
        return max(cache.values())