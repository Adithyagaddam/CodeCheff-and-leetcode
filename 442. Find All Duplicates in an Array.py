class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        s=[]
        for a,k in c.most_common():
            if k>=2:
                s.append(a)
        return s
