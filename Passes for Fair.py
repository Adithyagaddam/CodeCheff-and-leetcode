n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    if a+1<=b:
        print("YES")
    else:print("NO")
