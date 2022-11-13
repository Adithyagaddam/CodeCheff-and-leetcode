for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a==b:
        print("1")
    else:
        print(2*(b-a)+1)
