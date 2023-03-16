class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        s=[]
        for i in range(1,a+1):
                if a%i==0:
                    s.append(i)
        t=[]
        for i in range(1,b+1):
                if b%i==0:
                    t.append(i) 
        count=0 
        for i in range(len(s)):
            if s[i] in t:
                count+=1  
        return count
           
