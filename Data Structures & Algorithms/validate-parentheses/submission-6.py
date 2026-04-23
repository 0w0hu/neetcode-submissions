class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2o = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in c2o:
                if stack and c2o[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False