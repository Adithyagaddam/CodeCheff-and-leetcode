for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a>b:
        print("LOSS")
    elif a==b:
        print("NEUTRAL")
    else:
        print("PROFIT")
