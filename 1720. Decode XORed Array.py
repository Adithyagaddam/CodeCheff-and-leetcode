class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        result = [first] * (n + 1)
        for i in range(n):
	        result[i + 1] = encoded[i] ^ result[i]
        return result
