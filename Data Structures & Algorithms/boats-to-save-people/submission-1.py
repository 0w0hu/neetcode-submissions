class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        res = 0

        while l <= r:
            res += 1
            diff = limit - people[r]
            r -= 1
            if diff >= people[l]:
                l += 1
        return res