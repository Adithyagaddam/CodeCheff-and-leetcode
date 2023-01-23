class Solution:
    def reverseBits(self, n: int) -> int:
        k='{:032b}'.format(n)
        s=''.join(reversed(k))
        return int(s,2)
