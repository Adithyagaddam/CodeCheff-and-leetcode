for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    if a*c<b:
        print("YES")
    else:
        print("NO")
