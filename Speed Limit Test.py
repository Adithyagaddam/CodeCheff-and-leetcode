n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split(' '))
    s=a/c
    r=b/d 
    if s>r:
        print("Alice")
    elif s==r:
        print("Equal")
    elif s<r:
        print("Bob")
