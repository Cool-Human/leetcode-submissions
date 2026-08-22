class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        total = 0
        for i in operations:
            if i == '+':
                total += result[-2] + result[-1]
                result.append(result[-2] + result[-1])
            elif i == 'D':
                total += result[-1] * 2
                result.append(result[-1] * 2)
            elif i == 'C':
                total -= result.pop()
            else:
                result.append(int(i))
                total += int(i)
        return total