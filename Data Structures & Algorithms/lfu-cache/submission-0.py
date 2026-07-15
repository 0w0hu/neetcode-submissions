class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushtail(self, val):
        node = ListNode(val, self.tail.prev, self.tail)
        self.map[val] = node
        self.tail.prev = node
        node.prev.next = node 
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
        
    def pophead(self):
        res = self.head.next.val
        self.pop(self.head.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushtail(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfucnt = 0
        self.valmap = {}
        self.cntmap = defaultdict(int)
        self.listmap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.cntmap[key]
        self.cntmap[key] += 1
        self.listmap[cnt].pop(key)
        self.listmap[cnt+1].pushtail(key)

        if cnt == self.lfucnt and self.listmap[cnt].length() == 0:
            self.lfucnt += 1

    def get(self, key: int) -> int:
        if key not in self.valmap:
            return -1
        self.counter(key)
        return self.valmap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.valmap and len(self.valmap) == self.cap:
            res = self.listmap[self.lfucnt].pophead()
            self.valmap.pop(res)
            self.cntmap.pop(res)
        self.valmap[key] = value
        self.counter(key)
        self.lfucnt = min(self.lfucnt, self.cntmap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)