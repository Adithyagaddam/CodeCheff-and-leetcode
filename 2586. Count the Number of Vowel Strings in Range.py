class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        s=['a','e','i','o','u']
        count=0
        for i in range(left,right+1):
            t=[x for x in words[i]]
            if t[0] in s:
                if t[-1] in s:
                    count+=1
        return count
