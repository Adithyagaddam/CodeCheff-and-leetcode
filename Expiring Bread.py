for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    s=b*c
    if s>=a:
        print("Yes")
    else:
        print("No")
