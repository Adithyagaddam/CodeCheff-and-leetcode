# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l=l[::-1]
        p=[]
        for i in range(len(l)):
            if i!=n-1:
                p.append(l[i])
        p=p[::-1]
        print(p)
        t=ListNode(0)
        a=t
        for i in p:
            a.next=ListNode(i)
            a=a.next
        return t.next
