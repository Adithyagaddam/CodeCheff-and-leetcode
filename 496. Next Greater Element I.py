class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=[]
        for i in nums1:
            s=nums2.index(i)
            r=[]
            for j in range(s+1,len(nums2)):
                if i<nums2[j]:
                    r.append(nums2[j])
            
            if len(r)==0:
                k.append(-1)
            
            elif i<r[0]:
                k.append(r[0])
            else:
                k.append(-1)
        return k
