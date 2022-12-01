class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        k=len(s)
        s1=slice(0,len(s)//2)
        s2=slice(len(s)//2,len(s))
        r=s[s1]
        r=r.lower()
        t=s[s2]
        t=t.lower()
        vowels=0
        for i in r:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels=vowels+1
        vowels1=0
        for i in t:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels1=vowels1+1
        if vowels==vowels1:
            return True
