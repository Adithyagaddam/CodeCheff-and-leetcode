class Solution:
    def trailingZeroes(self, n: int) -> int:
        con=0
        while(n>=5):
            con+=n//5
            n=n//5
        return int(con)
