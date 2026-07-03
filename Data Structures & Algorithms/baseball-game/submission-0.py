class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == '+':
                result.append(result[-2] + result[-1])
            elif i == 'D':
                result.append(result[-1] * 2)
            elif i == 'C':
                result.pop()
            else:
                result.append(int(i))
        return sum(result)