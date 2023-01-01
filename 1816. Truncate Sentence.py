class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=list(s.strip().split())

        r=[]
        for i in range(k):
            r.append(s[i])
        r=' '.join(r)
        return str(r)
