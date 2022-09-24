n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    d,e,f=map(int,input().split(' '))
    if a>d and b>e:
        print("A")
    elif a>d and c>f:
        print("A")
    elif b>e and c>f:
        print("A")
    else:
        print("B")
