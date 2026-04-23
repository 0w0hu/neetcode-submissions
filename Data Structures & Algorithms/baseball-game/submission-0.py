class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for o in operations:
            if o == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                res += score
            elif o == "C":
                score = stack.pop()
                res = res - score
            elif o == "D":
                score = stack[-1]*2
                stack.append(score)
                res += score
            else:
                score = int(o)
                stack.append(score)
                res += score
        return res