n=int(input())
for i in range(n):
    s=int(input())
    a=list(map(int,input().strip().split()))
    k=[]
    for i in a:
        p=a.count(i)
        k.append(p)
    r=s-max(k)
    print(r)
