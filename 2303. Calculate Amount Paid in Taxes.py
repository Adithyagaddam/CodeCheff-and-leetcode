class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        p=[]
        t=[]
        for i in range(len(brackets)):
            p.append(brackets[i][0])
            t.append(brackets[i][1])
        s=[0]
        for i in range(len(p)):
            s.append((min(p[i],income)-s[i]))
            income=income-s[i]
        s.remove(s[0])
        r=[]
        for i in range(len(s)):
            r.append(s[i]*(t[i]))
        x=sum(r)
        return (x/100)
        
