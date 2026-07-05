class Solution:
    def isValid(self, s: str) -> bool:
        c2o = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in c2o:
                if not stack or c2o[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0