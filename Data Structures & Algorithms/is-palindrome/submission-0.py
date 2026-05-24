class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ''
        for i in s:
            if i.isalnum():
                output += i.lower()
        return output == output[::-1]

