n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    d=2*(a+180)
    print(d-b-c)
