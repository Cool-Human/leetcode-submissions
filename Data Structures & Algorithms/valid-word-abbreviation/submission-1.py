class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)

        while i < n and j < m:
            # Abbreviation numbers cannot start with zero.
            if abbr[j] == '0':
                return False

            if abbr[j].isalpha():
                # A letter must match the current word character.
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # Parse the full number.
                skip = 0
                while j < m and abbr[j].isdigit():
                    skip = skip * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1

                i += skip

        # Both strings must be fully consumed.
        return i == n and j == m