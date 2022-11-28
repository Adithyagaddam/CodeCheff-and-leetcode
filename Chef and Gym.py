for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    d=a+b
    if a>c:
        print(0)
    elif a<c and d<=c:
        print(2)
    else:
        print(1)
        
