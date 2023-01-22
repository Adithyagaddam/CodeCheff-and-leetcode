for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    k=b//a
    if (c-k)<0:
        print(0)
    else:print(c-k)
