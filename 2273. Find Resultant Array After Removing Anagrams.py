class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        s=['0']
        for i in range(len(words)):
            s.append(words[i]) 
        for i in range(len(s)):
            r=''.join(sorted(s[i]))
            t=''.join(sorted(s[i-1]))
            print(r)
            print(t)
            if r==t:
                words.remove(s[i])
        return words
