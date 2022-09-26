n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split(' '))
    if a<b:
        a+=c
    else:
        b+=c
    if a<b:
        a+=d
    else:
        b+=d
    if a>b:
        print("N")
    elif a==b:
        print("N")
    else:
        print("S")
