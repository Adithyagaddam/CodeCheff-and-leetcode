class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        t=s1.split()
        p=s2.split()
        q=Counter(t)
        r=Counter(p)
        for j,l in q.most_common():
            if l>1:
                for i in range(l):
                    t.remove(j)
        for j,l in r.most_common():
            if l>1:
                for i in range(l):
                    p.remove(j)
        s=[]
        for i in range(len(t)):
            if t[i] not in p:
                s.append(t[i])
        for i in range(len(p)):
            if p[i] not in t:
                s.append(p[i])
        return s
      
