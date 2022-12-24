for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    if a*b>d*c:
        print("NO")
    else:print("YES")
