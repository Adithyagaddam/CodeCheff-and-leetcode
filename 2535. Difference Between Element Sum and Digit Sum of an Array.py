class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        r=[]
        for i in range(len(nums)):
            k = 0
            for digit in str(nums[i]): 
                k+= int(digit)
            r.append(k)
        sum1=0
        for i in range(len(r)):
            sum1+=r[i]
        return sum-sum1
