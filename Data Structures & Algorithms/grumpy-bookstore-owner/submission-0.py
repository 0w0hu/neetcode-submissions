class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window = 0
        satisfy = 0
        max_window = 0
        for r in range(len(customers)):
            if grumpy[r] == 1:
                window += customers[r]
            else:
                satisfy += customers[r]
            
            if (r-l+1) > minutes:
                if grumpy[l] == 1:
                    window -= customers[l]
                l += 1
            max_window = max(window, max_window)
        return satisfy + max_window

