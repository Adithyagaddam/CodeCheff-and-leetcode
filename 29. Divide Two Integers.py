class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            a=(int(dividend/divisor))
            return min(max(-2147483648, a), 2147483647)
