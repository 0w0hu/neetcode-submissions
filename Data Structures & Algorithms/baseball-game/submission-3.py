class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for c in operations:
            if c == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                res += score
            elif c == "D":
                score = stack[-1] * 2
                stack.append(score)
                res += score
            elif c == "C":
                score = stack.pop()
                res -= score
            else:
                res += int(c)
                stack.append(int(c))
                
        return res