class Solution:
    def alternateDigitSum(self, n: int) -> int:
        p=str(n)
        t=[int(x) for x in p]
        r=[]
        for i in range(0,len(t),2):
            r.append(t[i])
        s=[]
        for i in range(1,len(t),2):
            s.append(t[i])
        return (sum(r)-sum(s))
