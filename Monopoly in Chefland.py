for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    k=max(a,b,c)
    if a==b and b==c and c==a:
        print("No")
    elif (a+b+c-k)<k:
        print("Yes")
    else:print("No")
