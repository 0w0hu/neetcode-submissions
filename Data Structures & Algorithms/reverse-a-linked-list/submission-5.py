# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next #store next element's address
            curr.next = prev #change the next element's to prev's address
            prev = curr #switch the prev to curr
            curr = tmp #switch the curr to curr.next
        return prev
