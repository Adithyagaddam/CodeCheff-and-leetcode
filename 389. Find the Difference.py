class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k=max(len(s),len(t))
        s=sorted(s)
        t=sorted(t)
        s.append(0)
        for i in range(k):
            if s[i]!=t[i]:
                return t[i]
