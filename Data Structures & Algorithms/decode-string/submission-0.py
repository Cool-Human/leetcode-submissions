class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0

        def help():
            res = ''
            k = 0
            while self.idx < len(s):
                c = s[self.idx]

                if c.isdigit():
                    k = k * 10 + int(c)
                elif c == '[':
                    self.idx += 1
                    res += k * help()
                    k = 0
                elif c == ']':
                    return res
                else:
                    res += c
                
                self.idx += 1
            return res
        
        return help()