class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        subCount = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            subCount[ord(s2[i]) - ord('a')] += 1
        
        for j in range(len(s1), len(s2)):
            
            if s1Count == subCount:
                return True
            
            remove_order = ord(s2[j - len(s1)]) - ord('a')
            subCount[remove_order] -= 1

            add_order = ord(s2[j]) - ord('a')
            subCount[add_order] += 1
        
        return s1Count == subCount