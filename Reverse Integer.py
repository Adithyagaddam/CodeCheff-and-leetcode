class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            a=x[::-1]
            p=f"{x[0]}{a[:-1]}"
            p=int(p)/1
            if p<(-2)**31:
                return 0
            else:
                return int(p)
        else:
            k= x[::-1]
            k=int(k)/1
            if k>((2)**31)-1:
                return 0
            else:
                return int(k)
