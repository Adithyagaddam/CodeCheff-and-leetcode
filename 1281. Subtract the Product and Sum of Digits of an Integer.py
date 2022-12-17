class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        n = list(map(int, str(n)))
        s=1
        k=0
        for i in range(len(n)):
            s=n[i]*s
        for i in range(len(n)):
            k=n[i]+k
        return s-k
