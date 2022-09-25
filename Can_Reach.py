=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    if a%c==0 and b%c==0:
        print("YES")
    else:print("NO")
