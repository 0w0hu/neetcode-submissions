class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        return cur.end

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        return True
        