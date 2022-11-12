for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    k=(d/100)*a
    s=k+a
    if b<=s<=c:
        print("YES")
    else:
        print("NO")
