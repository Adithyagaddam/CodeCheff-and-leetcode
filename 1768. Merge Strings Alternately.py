class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def gen():
            for w1, w2 in zip(word1, word2):
                yield from (w1, w2)
            if len(word1) < len(word2):
                yield word2[len(word1):]
            else:
                yield word1[len(word2):]

        return ''.join(gen())
