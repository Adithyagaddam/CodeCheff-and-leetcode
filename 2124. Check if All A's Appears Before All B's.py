class Solution:
    def checkString(self, s: str) -> bool:
        k=[x for x in s]
        if 'b' in k:
            s=k.index('b')
        if len(set(k))==1:
            return True

        count=0
        for i in range(s,len(k)):
            if k[i]=='a':
                count+=1
        if count==0:
            return True   
