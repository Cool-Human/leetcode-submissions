class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for age in details:
            if int(age[11:13]) > 60:
                res += 1
        return res