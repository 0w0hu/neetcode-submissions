# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_l, cur = dummy, head

        for _ in range(left-1):
            prev_l = cur
            cur = cur.next
        
        prev = None
        for _ in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        prev_l.next.next = cur
        prev_l.next = prev

        return dummy.next