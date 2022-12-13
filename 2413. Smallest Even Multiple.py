class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        while(i>0):
            if i%n==0 and i%2==0:
                return i
            i+=1
