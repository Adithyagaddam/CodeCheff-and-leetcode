import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(i for i in s if i.isalnum())
        s=s.lower()
        x=s[::-1]
        if x==s:
            return True
        else:
            return False
