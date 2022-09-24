n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    print(max(a+b,a+c,b+c))
