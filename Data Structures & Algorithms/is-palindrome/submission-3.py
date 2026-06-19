class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join([char.lower() for char in s if char.isalnum()])
        return text == text[::-1]