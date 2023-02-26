class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t=Counter(nums)
        print(t)
        for x in t.elements():
            if t[x]>1:
                return x
