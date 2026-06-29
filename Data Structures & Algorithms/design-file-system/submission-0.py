class TrieNode:
    def __init__(self):
        self.child = {}
        self.val = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split("/")[1:]
        cur = self.root
        for i, part in enumerate(parts):
            if i == len(parts)-1:
                if part in cur.child:
                    return False
                cur.child[part] = TrieNode()
                cur.child[part].val = value
                return True
            if part not in cur.child:
                return False
            cur = cur.child[part]

    def get(self, path: str) -> int:
        parts = path.split("/")[1:]
        cur = self.root

        for part in parts:
            if part not in cur.child:
                return -1
            cur = cur.child[part]
        return cur.val

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
