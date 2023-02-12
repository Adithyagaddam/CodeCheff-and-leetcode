# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1=[]
        while l1:
            lst1.append(l1.val)
            l1=l1.next
        lst1=lst1[::-1]
        lst2=[]
        while l2:
            lst2.append(l2.val)
            l2=l2.next   
        lst2=lst2[::-1]
        s1 = [str(i) for i in lst1]
        res1 = int("".join(s1))
        s2 = [str(i) for i in lst2]
        res2 = int("".join(s2))
        k=res1+res2
        res3 = [int(x) for x in str(k)]
        res3=res3[::-1]
        t=ListNode(0)
        a=t
        for i in res3:
            a.next=ListNode(i)
            a=a.next
        return t.next
