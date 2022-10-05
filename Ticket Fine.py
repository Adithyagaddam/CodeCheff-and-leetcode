n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    s=b-c
    x=s*a
    print(x)
