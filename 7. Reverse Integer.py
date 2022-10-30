class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            a=x[::-1]
            return f"{x[0]}{a[:-1]}"
        else:
            return x[::-1]
