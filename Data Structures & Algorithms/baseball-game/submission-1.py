class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for ops in operations:
            if ops == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                res += score
            elif ops == "C":
                score = stack.pop()
                res -= score
            elif ops == "D":
                score = stack[-1] * 2
                stack.append(score)
                res += score
            else:
                score = int(ops)
                stack.append(score)
                res += score
        return res