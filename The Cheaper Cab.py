n=int(input())
for TC in range(n):
    (a, b)=map(int,input().split(' '))
    if a<b:
        print("FIRST")
    elif a==b:
        print("ANY")
    else:
        print("SECOND")
