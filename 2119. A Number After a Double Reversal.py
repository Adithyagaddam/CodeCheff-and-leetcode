class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        k=str(num)
        p=int(k[::-1])
        t=str(p)
        s=int(t[::-1])
        if num==0:
            return True
        elif s==num:
            return True
        else:
            return False
