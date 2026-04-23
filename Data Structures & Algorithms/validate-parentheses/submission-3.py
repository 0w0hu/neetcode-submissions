class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2o = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in c2o:
                if stack and stack[-1] == c2o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                