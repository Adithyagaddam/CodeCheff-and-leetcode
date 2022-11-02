for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a*2==b*5:
        print("Either")
    elif a*2>b*5:
        print("Chocolate")
    else:
        print("Candy")
