class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                for k in range(i,j+1,1):
                    s+=arr[k]
                
        return s
