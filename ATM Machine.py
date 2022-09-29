n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    c=list(map(int,input().strip().split()))
    for i in range(a):
        if c[i]<=b:
           b=b-c[i]
           print(1,end='')
           
        else:
           print(0,end='')
    print('')
