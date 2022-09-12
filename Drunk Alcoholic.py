n=int(input())
for i in range(n):
    s=int(input())
    x=0
    for i in range(s+1):
        if i%2!=0:
            x+=3
        else:
            x-=1
    print(x+1)
