n=int(input())
for i in range(n):
    s=int(input())
    a=list(map(int,input().strip().split()))
    k=a.count(1)
    if k%2==0:
        print("YES")
    else:
        print("NO")
