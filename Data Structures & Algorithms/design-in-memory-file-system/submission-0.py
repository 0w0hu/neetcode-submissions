class TrieNode:
    def __init__(self):
        self.child = {}
        self.isFile = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def traverse(self, path):
        cur = self.root
        if path == "/":
            return cur
        
        parts = path.split("/")[1:]
        for part in parts:
            if part not in cur.child:
                cur.child[part] = TrieNode()
            cur = cur.child[part]
        return cur

    def ls(self, path: str) -> List[str]:
        cur = self.root
        if path == "/":
            return sorted(cur.child.keys())
        parts = path.split("/")[1:]
        for part in parts:
            cur = cur.child[part]
        if cur.isFile:
            return [parts[-1]]
        return sorted(cur.child.keys())

    def mkdir(self, path: str) -> None:
        self.traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.traverse(filePath)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.traverse(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
