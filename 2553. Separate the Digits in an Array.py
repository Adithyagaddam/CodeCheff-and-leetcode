class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        k=[]
        for i in  range(len(nums)):
                p=[int(i) for i in str(nums[i])]
                for i in range(len(p)):
                    k.append(p[i])
        return k
                   
