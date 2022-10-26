n=int(input())
for i in range(n):
    a,b,c=map(int,input().strip().split())
    if c%b==0:
        print("YES")
    else:
        print("NO")
