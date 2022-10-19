for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    if (a+b)%2!=0 or (c+b)%2!=0  or (a+c)%2!=0 :
        print("YES")
    else:
        print("NO")
