# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = prev
        right = slow
        res = 0

        while right:
            res = max(res, left.val+right.val)
            left = left.next
            right = right.next
        
        return res