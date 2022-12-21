for i in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=0
    for i in range(n):
        if a[i]>=x:
            s=b[i]+s
    print(s)
