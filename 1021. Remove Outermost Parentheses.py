class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        counter = 1
        i = 1
        while i < len(s):
            counter += 1 if s[i] == "(" else -1
            if counter != 0:
                result.append(s[i])
            else:
                counter = 1
                i += 1
            i += 1
        return "".join(result)
