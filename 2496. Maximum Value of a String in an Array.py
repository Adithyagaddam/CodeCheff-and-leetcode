class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        s=[]
        for i in range(len(strs)):
            if strs[i].isnumeric():
                s.append(int(strs[i]))
            else:
                s.append(len(strs[i]))
        return max(s)
