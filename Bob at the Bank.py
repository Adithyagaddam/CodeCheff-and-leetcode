n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split(' '))
    s=(b-c)*d 
    print(a+s)
