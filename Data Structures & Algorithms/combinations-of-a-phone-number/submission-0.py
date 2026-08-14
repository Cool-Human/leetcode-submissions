class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        nums = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        digits = list(digits)
        for digit in digits:
            if not res:
                res = nums[digit]
            else:
                ans = []
                for ch1 in res:
                    for ch2 in nums[digit]:
                        ans.append(ch1 + ch2)
                res = ans
        return res