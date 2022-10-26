n=int(input())
for i in range(n):
    a,b,c=map(int,input().strip().split())
    s=max(a,b,c)
    k=min(a,b,c)
    print(s-k)
