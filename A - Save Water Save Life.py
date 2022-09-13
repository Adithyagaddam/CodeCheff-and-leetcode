n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split(' '))
    s=b+(c//2)
    f=s*a 
    if f<=d:
        print("YES")
    else:
        print("NO")
