class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()[::-1]
        return (" ".join(k))
