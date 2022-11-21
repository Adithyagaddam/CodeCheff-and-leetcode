for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    k=a+c*d
    if b==k:
        print("filled")
    elif b<k:
        print("overFlow")
    else:
        print("Unfilled")
