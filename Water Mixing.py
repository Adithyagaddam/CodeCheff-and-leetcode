for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    if a==b:
        print("YES")
    elif a<b and (b-a)<=c:
        print("YES")
    elif b<a and (a-b)<=d:
        print("YES")
    else:
        print("NO")
