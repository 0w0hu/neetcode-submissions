class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.cap == 0: return False
        cur = ListNode(value, self.tail, self.tail.prev)
        self.tail.prev.next = cur
        self.tail.prev = cur
        self.cap -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.cap += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.cap == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()