class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=text.count("b")
        a=text.count("a")
        l=text.count("l")
        o=text.count("o")
        n=text.count("n")
        return min(b,a,l//2,o//2,n)
