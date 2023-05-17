class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        k=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                k.append(nums1[i])
        if len(k)>0:
            return min(k)
        else:
            s=[min(nums1),min(nums2)]
            s.sort()
            return int(str(s[0])+str(s[1]))
