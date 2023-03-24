class Solution:
    def splitNum(self, num: int) -> int:
        p=[int(x) for x in str(num)]
        p.sort()
        r=[]
        t=[]
        for i in range(0,len(p),2):
            r.append(str(p[i]))
        for i in range(1,len(p),2):
            t.append(str(p[i]))
        e=int(''.join(r))
        s=int(''.join(t))
        return e+s
