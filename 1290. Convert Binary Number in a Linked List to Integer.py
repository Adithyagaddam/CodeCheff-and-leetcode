# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        s=[]
        for i in l:
            s.append(str(i))
        k=''.join(s)
        return int(k,2)
