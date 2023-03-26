class Solution:
    def greatestLetter(self, s: str) -> str:
        t=''.join(sorted(s,reverse=True))
        print(t)
        
        k=[x for x in t]
    
        for i in range(len(k)):
            r=k[i].upper()
            l=k[i].lower()
            if r in k:
                if l in k:
                    return r
        else: return ""
