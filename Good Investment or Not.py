for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a>=2*b:
        print("YES")
    else:
        print("NO")
