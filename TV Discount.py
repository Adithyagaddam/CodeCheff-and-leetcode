for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    k=a-c
    p=b-d
    if k>p:
        print("Second")
    elif k==p:
        print("Any")
    else:
        print("First")
