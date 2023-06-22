# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import *
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append(root)
        s=[]
        while q:
            k=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp:
                    k.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if k:
               s.append(mean(k))
        return s
