for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    if a==b or b==c or a==c:
        print("NO")
    else:
        print("YES")
