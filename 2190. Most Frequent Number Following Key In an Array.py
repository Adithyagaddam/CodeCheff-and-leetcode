class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        k=[]
        for i in range(nums.index(key)+1,len(nums)):
            k.append(nums[i])
        s=Counter(k)
        t=[]
        for j,l in s.most_common():
            t.append([j,l])
        p=sorted(t, key=itemgetter(1),reverse=True)
        return p[0][0]
