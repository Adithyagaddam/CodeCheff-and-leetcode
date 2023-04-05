class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s=[]
        t=Counter(nums)
        for j,l in t.most_common():
            if l%2==0:
                s.append(True)
            else:
                s.append(False)
        r=list(set(s))
        if len(list(set(s)))==1 and r[0]==True:
            return True
        else:
            return False
