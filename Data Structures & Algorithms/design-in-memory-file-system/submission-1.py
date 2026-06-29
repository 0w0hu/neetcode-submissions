class TrieNode:
    def __init__(self):
        self.child = {}
        self.isFile = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def traverse(self, path, create=False):
        cur = self.root
        if path == "/":
            return cur
        
        parts = path.split("/")[1:]
        for part in parts:
            if part not in cur.child:
                if create:
                    cur.child[part] = TrieNode()
                else:
                    return None
            cur = cur.child[part]
        return cur

    def ls(self, path: str) -> List[str]:
        node = self.traverse(path)
        if node.isFile:
            return [path.split("/")[-1]]
        return sorted(node.child.keys())

    def mkdir(self, path: str) -> None:
        self.traverse(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.traverse(filePath, True)
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
