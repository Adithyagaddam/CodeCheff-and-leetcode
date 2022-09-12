n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    if (a==0 and b==0 and c==0) or (a==1 and b==1 and c==1):
        print(0)
    else:
        print(1)
