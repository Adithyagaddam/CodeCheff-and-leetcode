n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    if a==0:
        print(0)
    elif a!=0 and a%b!=0:
        print(-1)
    elif a%b==0:
        print(a//b)
