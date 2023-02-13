# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        l1=[]
        l2=[]
        while list1:
            l1.append(list1.val)
            list1=list1.next
        while list2:
            l2.append(list2.val)
            list2=list2.next
        l3=l1+l2
        print(l3)
        l3.sort()
        t=ListNode(0)
        s=t
        for i in l3:
            s.next=ListNode(i)
            s=s.next
        return t.next
