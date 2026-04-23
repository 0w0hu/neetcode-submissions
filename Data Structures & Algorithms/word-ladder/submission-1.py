class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = (wordList)
        if endWord not in wordList:
            return 0
        
        q = deque()
        q.append((beginWord,1))
        visit = {beginWord}

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    new_word = word[:i]+c+word[i+1:]
                    if new_word in wordList and new_word not in visit:
                        visit.add(new_word)
                        q.append((new_word, step+1))
                        
        return 0