class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        s=[]
        q.append(root)
        while q:
            k=[]
            for i in range(len(q)):
                temp=q.popleft()
                
                if temp:
                    k.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if k:
                s.append(sum(k))
        mx=max(s)
        return s.index(mx)+1  
