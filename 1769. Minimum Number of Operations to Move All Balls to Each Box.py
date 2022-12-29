class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        for i in range(len(boxes)):
            a=0
            for j in range(len(boxes)):
                if(i!=j and boxes[j]=="1"):
                    a+=abs(j-i)
            l.append(a)
        return l
