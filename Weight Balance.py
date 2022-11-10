for i in range(int(input())):
    a,b,c,d,e=map(int,input().strip().split())
    f=b-a
    if (c*e)<=f<=(d*e):
        print("1")
    else:
        print("0")
