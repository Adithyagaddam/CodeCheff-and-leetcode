class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        v=[x for x in s]
        r=list(set(v))
        p=[]
        for i in range(len(r)):
            t=v.count(r[i])
            p.append(t)
        if len(set(p))==1:
            return True
        
