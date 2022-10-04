n=int(input()) 
for i in range(n):
    a,b=map(int,input().strip().split())
    if a>=b:
        print(7-a)
    else:
        print(7-b)
