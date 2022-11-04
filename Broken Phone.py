for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a>b:
        print("NEW PHONE")
    elif a==b:
        print("ANY")
    else:print("REPAIR")
