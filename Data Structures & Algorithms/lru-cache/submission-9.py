class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        prev, nxt = self.head, self.head.next

        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
