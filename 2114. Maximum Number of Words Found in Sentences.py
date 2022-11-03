class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        s=[]
        for i in range(len(sentences)):
            p=len(sentences[i].split())
            s.append(p)
        return max(s)
            
