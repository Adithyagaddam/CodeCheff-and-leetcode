class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split() 
        s=len(a)
        return len(a[s-1])
