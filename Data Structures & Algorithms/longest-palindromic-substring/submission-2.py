class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = 0
        best_right = 0  # inclusive

        for i in range(len(s)):
            # Odd-length palindrome: center is s[i]
            left, right = i, i

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                if right - left > best_right - best_left:
                    best_left = left
                    best_right = right

                left -= 1
                right += 1

            # Even-length palindrome: center is between s[i] and s[i + 1]
            left, right = i, i + 1

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                if right - left > best_right - best_left:
                    best_left = left
                    best_right = right

                left -= 1
                right += 1

        return s[best_left:best_right + 1]