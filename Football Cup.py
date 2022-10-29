for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a==0 or b==0:
        print("NO")
    elif a==b:
        print("YES")
    else:
        print("NO")
    
