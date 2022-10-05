n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().strip().split())
    if a+b<=c+d:
        print(a+b)
    else:
        print(c+d)
