n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    if (b/a)*100>=50:
        print("YES")
    else:
        print("NO")
