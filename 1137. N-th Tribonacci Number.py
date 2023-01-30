class Solution:
    def tribonacci(self, n: int) -> int:
        ar=[0,1,1]
        sum=0
        for i in range(3,n+1):
                ar.append((ar[i-1]) + (ar[i-2])+(ar[i-3]))
        for i in range(n):
            sum+=ar[i]
        return ar[n]
