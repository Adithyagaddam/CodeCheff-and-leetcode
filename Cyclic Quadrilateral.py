# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    if a+c==180 and b+d==180:
        print("YES")
    else:
        print("NO")
