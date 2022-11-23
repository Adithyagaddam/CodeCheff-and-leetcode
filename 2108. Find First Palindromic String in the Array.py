class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        p=[]
        for i in range(len(words)):
            k=words[i]
            s=k[::-1]
            if k==s:
                p.append(words[i])
        if len(p)==0:
            return ""
        else:
            return p[0]
