for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    k=max(a,b,c)
    if (a+b+c-k)<k :
        print("YES")
    else:
        print("NO")
