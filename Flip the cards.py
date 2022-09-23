n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    
    if a==b or b==0:
        print(0)
    elif a-b>a/2:
        print(b)
    else:
        print(a-b)
