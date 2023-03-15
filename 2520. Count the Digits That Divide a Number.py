class Solution:
    def countDigits(self, num: int) -> int:
        t=str(num)
        p=[int(x) for x in t]
        count=0
        for i in range(len(p)):
            if num%p[i]==0:
                count+=1
        return count
