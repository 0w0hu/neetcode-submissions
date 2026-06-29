class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.end = True

    def search(self, word: str) -> bool:
        
        def helper(node, j):
            cur = node
            for i in range(j, len(word)):
                w = word[i]
                if w == ".":
                    for c in cur.child:
                        if helper(cur.child[c], i+1):
                            return True
                    return False

                else:
                    if w not in cur.child:
                        return False
                    cur = cur.child[w]
            return cur.end

        return helper(self.root, 0)