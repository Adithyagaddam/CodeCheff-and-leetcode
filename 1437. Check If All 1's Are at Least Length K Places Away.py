class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        s=[]
        for i in range(len(nums)):
            if nums[i]==1:
                s.append(i)
        
        print(s)
        p=[]
        for i in range(len(s)-1):
            p.append(s[i+1]-s[i]-1)
        print (p)
        for i in p:
            if i<k:
                return False
        return True
